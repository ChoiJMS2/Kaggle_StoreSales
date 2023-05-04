# -*- coding:utf-8 -*-
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

import streamlit as st
from pathlib import Path

from utils import date_select

@st.cache_data
def load_data():
    comp_dir = Path('data')
    train = pd.read_csv(comp_dir / 'train_sample_201516.csv')
    stores = pd.read_csv(comp_dir / 'stores.csv')
    oil = pd.read_csv(comp_dir / 'oil.csv')
    transactions = pd.read_csv(comp_dir / 'transactions.csv')
    holidays_events = pd.read_csv(comp_dir / 'holidays_events.csv')

    return train, stores, oil, transactions, holidays_events

def run_eda():
    # train, stores, oil, transactions, holidays_events = load_data()
    select = st.sidebar.selectbox('submenu', [
        '전처리', 'Total Sales', 'Promotion', 'Holidays', 'Oil'] )
    if select == '전처리':
        st.markdown("## 전처리")

    elif select == 'Total Sales':
        st.markdown('## 총매출')

    elif select == 'Promotion':
        st.markdown("## 프로모션")

    elif select == 'Holidays':
        st.markdown("## 공휴일")

    elif select == 'Oil':
        sub = st.sidebar.selectbox("submenu",['일일유가', '상관관계'])
        if sub == '일일유가':
            st.markdown("## 일일유가")
            # daily_oil()
        elif sub == '상관관계':
            st.markdown("## 상관관계")
            Oil_corr_tab, Oil_fs_tab = st.tabs(['CORR', 'FS'])

            with Oil_corr_tab:
                st.markdown('### Corr')
                 # oil_corr()

            with Oil_fs_tab:
                st.markdown('### FS')
                 # oil_fs()
        else:
            print('error...')
    else:
        print("error...")




