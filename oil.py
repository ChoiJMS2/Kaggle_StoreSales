# -*- coding:utf-8 -*-
# 기본 패키지
import numpy as np
import pandas as pd
import os
import gc
import warnings

# 회귀분석 패키지
import statsmodels.api as sm

# 시각화 패키지
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import streamlit as st

def run_oil_sales(train, stores, oil, transactions):
    # object타입을 datetime 형식으로 바꾸기
    transactions = transactions.sort_values(["store_nbr", "date"])

    train["date"] = pd.to_datetime(train.date)
    transactions["date"] = pd.to_datetime(transactions.date)
    oil["date"] = pd.to_datetime(oil.date)

    # 데이터 타입 변환
    train.onpromotion = train.onpromotion.astype("float16")
    train.sales = train.sales.astype("float32")
    stores.cluster = stores.cluster.astype("int8")

    # train 데이터에서 "date"와 "store_nbr" 컬럼 기준으로 sales 컬럼을 합치고 인덱스 리셋, transactions + temp 합쳐서 각 매장의 매출과 거래량 간의 상관관계를 분석
    temp = pd.merge(train.groupby(["date", "store_nbr"]).sales.sum().reset_index(), transactions, how="left")

    # 위의 석유 가격 데이터를 dcoilwtico 컬럼을 기준으로로 일일 빈도로 다시 샘플링, sum()을 통해 해당 일자의 총합 구하고 reset_index()를 통해 index를 초기화
    oil = oil.set_index("date").dcoilwtico.resample("D").sum().reset_index()

    # 0값(결측치)이 있는 경우에는 앞뒤 데이터를 활용하여 보간 => 데이터의 흐름을 유지하면서 결측치를 대체하는 방법
    oil["dcoilwtico"] = np.where(oil["dcoilwtico"] == 0, np.nan,
                                 oil["dcoilwtico"])  # dcoilwtico 컬럼이 0인 값을 결측치(np.nan)로 변경
    oil["dcoilwtico_interpolated"] = oil.dcoilwtico.interpolate()  # 결측치를 보간하는 interpolate() 함수

    # date 컬럼과 재구성한 컬럼들(value)과 Legend 컬럼(dcoilwtico)으로 구성된 데이터프레임 p 생성
    p = oil.melt(id_vars=['date'] + list(oil.keys()[5:]), var_name='Legend')

    st.markdown("""
        - Higher oil prices tend to make production more expensive for businesses, just as they make it more expensive for households to do the things they normally do. 
        - It turns out that oil and gasoline prices are indeed very closely related. 
        - At a consumer level, lower oil prices means more purchasing power for the customers. \n
        """)
    # p 데이터프레임을 Legend 컬럼(dcoilwtico)을 기준으로 내림차순 정렬하고, date 컬럼을 기준으로 오름차순 정렬
    fig = px.line(p.sort_values(["Legend", "date"], ascending=[False, True]), x='date', y='value', color='Legend',
            title="Daily Oil Price")
    st.plotly_chart(fig)

    # 사용자 정의 함수 oil_corr : 일일 석유 가격과 다른 변수들간의 스피어만 상관계수를 계산하여 출력

    # temp 데이터프레임과 oil 데이터프레임을 date 컬럼을 기준으로 병합(left join) => 병합한 결과 데이터프레임 temp에 dcoilwtico 컬럼이 추가
    temp = pd.merge(temp, oil, how="left")  # 판매량(sales) 및 거래량(transactions) 상관관계 분석
    print("일일 석유가격 상관관계 분석")

    # temp 데이터프레임에서 store_nbr과 dcoilwtico 컬럼을 제외한 나머지 컬럼들의 스피어만 상관계수를 계산
    print(temp.drop(["store_nbr", "dcoilwtico"], axis=1).corr("spearman").dcoilwtico_interpolated.loc[
              ["sales", "transactions"]],
          "\n")  # 계산한 상관계수 중 dcoilwtico_interpolated 컬럼과 sales, transactions 컬럼의 상관계수를 출력
    st.markdown("📌 **Interpret:**\n"
                "- This explains why there's an increase in average sales since mid-2015. \n"
                "- Oil prices will be used as a variable for training."
                 )
    st.markdown("\n")
    # 일일 석유 가격과 거래량, 일일 석유 가격과 매출 간의 상관관계 시각화
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))  # 그래프를 1행 2열로 배치, 크기를 (15,5). fig는 전체 그래프를 의미, axes는 각 그래프를 의미
    temp.plot.scatter(x="dcoilwtico_interpolated", y="transactions", ax=axes[
        0])  # 데이터프레임에서 "dcoilwtico_interpolated" 컬럼을 x축, "transactions" 컬럼을 y축인 산점도 그래프를 axes[0]에 그림
    temp.plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[1], color="r")
    axes[0].set_title('Daily oil price & Transactions', fontsize=15)  # 일일 석유 가격과 거래량
    axes[1].set_title('Daily Oil Price & Sales', fontsize=15);  # 일일 석유 가격과 매출
    st.pyplot(fig)
    st.markdown("""
    - Ecuador is an oil-dependent country. 
- Let's look at the correlation between sales and volume.
- The correlation value is not strong, but the sign of sales is negative. 
- If the daily oil price is high we would expect that the Ecuadorian economy is not doing well.
- So the price of the product will increase and sales will decrease. There is a negative relationship here.
    """)

    # 사용자 정의 함수 oil_fs : 일일 유가가 제품의 판매량에 영향을 미치는지, 어느 정도의 영향을 미치는지 확인

    #  train 데이터에서 날짜(date)와 제품군(family) 별 총 판매량(sales)을 합산, oil 데이터에서 유가(dcoilwtico_interpolated)를 가져와 merge, 각 제품군과 유가 간의 spearman 상관관계를 계산
    a = pd.merge(train.groupby(["date", "family"]).sales.sum().reset_index(), oil.drop("dcoilwtico", axis=1),
                 how="left")
    c = a.groupby("family").corr("spearman").reset_index()
    c = c[c.level_1 == "dcoilwtico_interpolated"][["family", "sales"]].sort_values("sales")

    fig, axes = plt.subplots(7, 5, figsize=(20, 20))
    for i, fam in enumerate(c.family):
        if i < 6:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[0, i - 1])
            axes[0, i - 1].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[0, i - 1].axvline(x=45, color='r', linestyle='--')
        if i >= 6 and i < 11:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[1, i - 6])
            axes[1, i - 6].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[1, i - 6].axvline(x=45, color='r', linestyle='--')
        if i >= 11 and i < 16:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[2, i - 11])
            axes[2, i - 11].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[2, i - 11].axvline(x=45, color='r', linestyle='--')
        if i >= 16 and i < 21:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[3, i - 16])
            axes[3, i - 16].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[3, i - 16].axvline(x=45, color='r', linestyle='--')
        if i >= 21 and i < 26:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[4, i - 21])
            axes[4, i - 21].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[4, i - 21].axvline(x=45, color='r', linestyle='--')
        if i >= 26 and i < 31:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[5, i - 26])
            axes[5, i - 26].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[5, i - 26].axvline(x=45, color='r', linestyle='--')
        if i >= 31:
            a[a.family == fam].plot.scatter(x="dcoilwtico_interpolated", y="sales", ax=axes[6, i - 31])
            axes[6, i - 31].set_title(fam + "\n Correlation:" + str(c[c.family == fam].sales.iloc[0])[:6], fontsize=12)
            axes[6, i - 31].axvline(x=45, color='r', linestyle='--')

    # "GROCERY I", "BEVERAGES" 등의 제품군은 유가와 양의 상관관계
    #  "EGGS"와 같은 제품군은 유가와 음의 상관관계

    plt.tight_layout(pad=5)
    plt.suptitle("Daily Oil Product & Total Family Sales \n", fontsize=20);  # 일일 석유 제품 & 모든 제품군 판매량
    st.pyplot(fig)
    st.markdown( "📌 **Interpret:**\n"
        " - You should never decide what you will do by looking at a graph or result.\n" 
    " - You are supposed to change your view and define new hypotheses.\n"
  " - We would have been wrong if we had looked at some simple outputs just like above and we had said that there is no relationship with oil prices and let's not use oil price data. "

    )
