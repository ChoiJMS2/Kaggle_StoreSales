# store
family_df2 = np.round(
    df_data.loc[df_data['store_nbr'] == store_nbr, :].groupby('family')['sales'].agg('mean').sort_values(
        ascending=False), 1)
col1 = st.selectbox('Select Column 1', df_data['family'].unique(), key="family_col1")
col2 = st.selectbox('Select Column 2', df_data['store_nbr'].unique(), key="store_col2")
fig2 = go.Figure(go.Bar(
    x=family_df2.values,
    y=family_df2.index,
    orientation='h',
    marker=dict(
        color=color2
    )
))

# Customize the layout
fig2.update_layout(
    title=f'Sales for Store : No.{store_nbr} ',
    xaxis_title='Mean of Sales',
    yaxis_title='Family',
    plot_bgcolor='white',
    width=800,
    height=400,
    margin=dict(l=20, r=20, t=60, b=20)
)

st.plotly_chart(fig2)
