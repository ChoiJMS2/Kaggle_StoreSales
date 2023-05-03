# -*- coding:utf-8 -*-

import pandas as pd

# Date Selection
def date_select(data, col):
    data[col] = pd.to_datetime(data[col])
    data['year'] = data[col].dt.year
    data['month'] = data[col].dt.month
    data['day'] = data[col].dt.day

    new_df = data.loc[data['year'].isin([2015, 2016]), :]
    return new_df