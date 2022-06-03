from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sb

def run_eda():
    st.subheader('데이터 분석')

    morny_df = pd.read_csv('data/monry.csv',index_col=0,encoding='ISO-8859-1')

    radio_menu = ['데이터프레임','통계치']
    selected = st.radio('선택하세요',radio_menu)

    if selected == radio_menu[0] :
        st.dataframe(morny_df)
    elif selected == radio_menu[1]:
        st.dataframe(morny_df.describe())

    col_list = morny_df.columns
    selected_list = st.multiselect('컬럼을 클릭하여 상관계수 알아보기',col_list)

    if len(selected_list) > 1:

        st.text('선택하신 컴럼끼리의 상관계수입니다.')
        st.dataframe( morny_df[selected_list].corr() )

        fig1 = plt.figure()
        sb.heatmap(data= morny_df[selected_list].corr(), annot=True, fmt='.2f', vmax= 1, vmin=-1, cmap='coolwarm',linewidths=0.5)
        st.pyplot(fig1)