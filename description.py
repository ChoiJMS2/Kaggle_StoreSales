# -*- coding:utf-8 -*-
import streamlit as st
from PIL import Image
def run_description():
    img = Image.open("image/123.jpg")
    st.image(img)
    tab1, tab2 = st.tabs(['소개', '데이터 설명'])
    with tab1:
        st.markdown("[kaggle Store Sales](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)")
        st.markdown("### 대회 목표 \n"
                    "- 시계열 예측을 사용하여 에콰도르에 본사를 둔 대형 식료품 소매업체 '코퍼라시온 파보리타(Corporación Favorita)'의 데이터를 바탕으로 매장 매출을 예측 \n"
                    "- 여러 Favorita 매장에서 판매되는 수천 가지 품목의 판매 단가를 더 정확하게 예측하는 모델을 구축함  \n"
                    "- 날짜, 매장 및 품목 정보, 프로모션, 판매 단가로 구성된 접근하기 쉬운 학습 데이터 세트를 통해 머신 러닝 기술을 연습 함")
        st.markdown("------------")
        st.markdown("### 평가 지표 \n"
                    "- 평균제곱로그오차(Root Mean Squared Logarithmic Error) \n")
        st.latex(r'''
               {RMSLE} = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n}}
               ''')
        st.markdown(" - $n$ : 총 인스턴스 수\n"
                    " - $\hat{y}$ : 인스턴스 (i)에 대한 대상의 예측 값\n"
                    " - $y_i$ : 인스턴스 (i)에 대한 대상의 실제 값\n"
                    " - $log$ : 자연 로그\n"
                    )
        st.markdown("### 문제해결 프로세스 \n")

        img = Image.open("image/kaggle.jpg")
        st.image(img)
        st.markdown("------------")
        st.markdown("### 데이터 이해\n"
                    "- 2013년부터 2017년까지의 판매 데이터\n"
                    "- 54개의 매장, 8개의 제품 카테고리/제품군(family)\n"
                    "- 각 매장은 7일에 한 번씩 판매 데이터를 기록\n"
                    "- 데이터에는 판매량(sales)과 기타 매장 정보(store_nbr, family, date 등)가 포함\n")
        with tab2:
            st.markdown("""- **train.csv**
  - The training data, comprising time series of features store_nbr, family, and onpromotion as well as the target sales.
  - store_nbr identifies the store at which the products are sold.
  - family identifies the type of product sold.
  - sales gives the total sales for a product family at a particular store at a given date. Fractional values are possible since products can be sold in fractional units (1.5 kg of cheese, for instance, as opposed to 1 bag of chips).
  - onpromotion gives the total number of items in a product family that were being promoted at a store at a given date.

- **stores.csv**
  -  Store metadata, including city, state, type, and cluster.
  - cluster is a grouping of similar stores.

- **oil.csv**
  - Daily oil price.
  - Includes values during both the train and test data timeframes.
    -(Ecuador is an oil-dependent country and it's economical health is highly vulnerable to shocks in oil prices.)

- **holidays_events.csv**
  - Holidays and Events, with metadata
  - A holiday that is transferred officially falls on that calendar day, but was moved to another date by the government. 
  To find the day that it was actually celebrated, look for the corresponding row where type is Transfer.
  - Days that are type Bridge are extra days that are added to a holiday.
  - Additional holidays are days added a regular calendar holiday, for example, as typically happens around Christmas.

- **Additional Notes**
  - Wages in the public sector are paid every two weeks on the 15 th and on the last day of the month. Supermarket sales could be affected by this.
  - A magnitude 7.8 earthquake struck Ecuador on April 16, 2016. People rallied in relief efforts donating water and other first need products which greatly affected supermarket sales for several weeks after the earthquake.""")