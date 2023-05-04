# -*- coding:utf-8 -*-
import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image

@st.cache_data
def load_data():
    img_path = "image/datacode.png"
    img = Image.open(img_path)
    st.image(img, caption='Sales Image')
    comp_dir = Path('data')

    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')
    return train, stores, oil, transactions, holidays_events
def run_data():

    train, stores, oil, transactions, holidays_events = load_data()
    tab1, tab2 = st.tabs(['데이터', '정의서'])
    menu = st.sidebar.selectbox("Submenu", ['Train','Stores', 'Oil', 'Transactions','Holidays_events'])

    if menu == 'Train':
        with tab1:
            st.markdown("## Train 데이터")
            st.dataframe(train, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)
        with tab2:
            st.markdown("## Train 데이터")
            st.markdown("Train 데이터는~~~~~ ")
    elif menu == 'Stores':
        with tab1:
            st.markdown("## Stores 데이터")
            st.dataframe(stores, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)
        with tab2:
            st.markdown("## Store 데이터")
            st.markdown("Store 데이터는~~~~~ ")
    elif menu == 'Oil':
        with tab1:
            st.markdown("## Oil 데이터")
            st.dataframe(oil, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)
        with tab2:
            st.markdown("## Oil 데이터")
            st.markdown("Oil 데이터는~~~~~ ")
    elif menu == 'Transactions':
        with tab1:
            st.markdown("## Transactions 데이터")
            st.dataframe(transactions, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)
        with tab2:
            st.markdown("## Transactions  데이터")
            st.markdown("Transactions  데이터는~~~~~ ")
    elif menu == 'Holiday Events':
        with tab1:
            st.markdown("## Holiday Events 데이터")
            st.dataframe(holidays_events, use_container_width=True)
            st.markdown('<hr>', unsafe_allow_html=True)
        with tab2:
            st.markdown("## Holiday Events 데이터")
            st.markdown("Holiday Events 데이터는~~~~~ ")
    else:
        print("error...")


