# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from description import run_description
from eda import run_eda
from PIL import Image
from data import run_data
from family_eda import run_Show


def main():

    st.set_page_config(page_title='Store Sales',
                       layout='wide',
                       page_icon='💹')
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Description', 'Data', 'EDA', 'STAT'],
                               icons=['house', 'card-checklist', 'card-checklist', 'bar-chart', 'clipboard-data'],
                               menu_icon="cast", default_index=0, orientation='vertical')
    if selected == 'Home':
        img = Image.open("image/mak.png")
        st.image(img, width=500)

        st.markdown("<h1 style='color: red;'>Store Sales - Time Series Forecasting</h1>", unsafe_allow_html=True)

        data = {'조원': ['최정안', '최재명', '권용석', '윤용준', '이건용', '이경철'],
            '기술': ['분석, 기획', '분석, 전처리', '분석, 대시보드','대시보드, PPT', '자료조사,대시보드', '', ]}
        df = pd.DataFrame(data)
        st.table(df)

        st.markdown("### 분석 언어툴")
        col1, col2, col3 = st.columns(3)
        with col1:
            img = Image.open("image/st1.png")
            st.image(img, width=200)
        with col2:
            img1 = Image.open("image/py1.png")
            st.image(img1, width=200)
        with col3:
            img2 = Image.open("image/py2.png")
            st.image(img2, width=200)



        st.markdown("### 프로젝트 개요\n\n"
                    "- 시계열 예측을 사용하여 에콰도르에 본사를 둔 대형 식료품 소매업체 '코퍼라시온 파보리타(Corporación Favorita)'의 데이터를 바탕으로 매장 매출을 예측 \n\n"
                    "- 여러 Favorita 매장에서 판매되는 수천 가지 품목의 판매 단가를 더 정확하게 예측하는 모델을 구축함  \n\n"
                    "- 날짜, 매장 및 품목 정보, 프로모션, 판매 단가로 구성된 접근하기 쉬운 학습 데이터 세트를 통해 머신 러닝 기술을 연습 하기 위함 목적")

        st.markdown("### 진행기간 \n"
                    "- 2023.04.20~05.17")

        st.markdown("### 분석 목적")
        st.markdown(" - 매장의 과거 판매 데이터에 대한 통찰력을 얻고 해당 정보를 사용하여 향후 판매 추세를 예측함\n\n"
                    " - 매장은 재고 관리, 마케팅 전략 및 전반적인 비즈니스 계획에 대해 더 많은 정보에 입각한 결정을 내림\n\n"
                    " - 판매 데이터의 패턴과 추세를 분석함으로써 프로젝트 팀은 계절성이나 외부 이벤트와 같이 판매 변화에 기여할 수 있는 요인을 식별함\n\n"
                    " - 궁극적으로 매장이 운영을 최적화하고 재무 성과를 개선하는 데 도움이 되는 실행 가능한 통찰력을 제공함")

        st.markdown("### 매출 변화 추이 파악 및 예측")

        st.markdown("### 최종 예측 모델링")
        col1, col2 = st.columns(2)
    elif selected == 'Description':
        run_description()
    elif selected == 'Data':
        run_data()
    elif selected == 'EDA':
        run_eda()
    elif selected == 'STAT':
        run_Show()
    else:
        st.write('error..')

if __name__ == "__main__":
    main()