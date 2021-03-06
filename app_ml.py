import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import joblib
from sklearn.preprocessing import MinMaxScaler

def run_ml():
    st.subheader('대출금액 예측하기')

    heart_df = pd.read_csv('data/monry.csv',index_col=0,encoding='ISO-8859-1')
    # 예측하기 위해서 필요한 파일들을 불러와야 된다.
    # 이 예에서는, 인공지능파일, X 스케일러 파일, y 스케일러파일
    # 3개를 불러와야 한다.

    regressor = joblib.load('data/Mon_regressor.pkl')
    scaler_X = joblib.load('data/Mon_scaler_X.pkl')
    scaler_y =joblib.load('data/Mon_scaler_y.pkl')

    Gender = st.radio('성별을 선택해주세요.',['남자','여자'])
    if Gender == '남자' :
        Gender = 1
    elif Gender == '여자' :
        Gender = 0
    Married	= st.radio('결혼유무를 선택해주세요.',['기혼','미혼'])
    if Married == '기혼' :
        Married = 1
    elif Married == '미혼' :
        Married = 0
    Dependents = st.selectbox('부양가족을 선택해주세요.',[1,2,3,4])
    if Married == '1' :
        Married = 1
    elif Married == '2' :
        Married = 2
    elif Married == '3' :
        Married = 3
    elif Married == '4' :
        Married = 4
    Education = st.radio('대학교 졸업 유무를 선택해주세요',['졸업','미졸업'])
    if Education == '졸업' :
        Education = 1
    elif Education == '미졸업' :
        Education = 0
    Self_Employed = st.radio('자영업자이신가여?',['맞다','아니다'])
    if Self_Employed == '맞다' :
        Self_Employed = 1
    elif Self_Employed == '아니다' :
        Self_Employed = 0
    ApplicantIncome = st.number_input('신청인의 연 평균 소득(만원)을 입력해주세요.',0,)
    if ApplicantIncome >= 3000 :
        ApplicantIncome = 3
    elif ApplicantIncome >= 2000 :
        ApplicantIncome = 2
    elif ApplicantIncome >= 1000 :
        ApplicantIncome = 1    
    else :
        ApplicantIncome = 0
    CoapplicantIncome = st.number_input('부양자의 연 평균 소득(만원)을 입력해주세요.',0,)
    if CoapplicantIncome >= 3000 :
        CoapplicantIncome = 3
    if CoapplicantIncome >= 2000 :
        CoapplicantIncome = 2
    if CoapplicantIncome >= 1000 :
        CoapplicantIncome = 1
    else :
        CoapplicantIncome = 0
    LoanAmount = st.number_input('원하는 대출금액(만원)을 입력해주세요.',0,3000)
    if LoanAmount >= 100 :
        LoanAmount = 1
    Loan_Amount_Term = st.slider('납부기간을 정해주세요', 12, 360)
    Credit_History = st.radio('연체유무가 있으신가여?',['있다','없다'])
    if Credit_History == '없다' :
        Credit_History = 1
    else :
        Credit_History = 0
    Property_Area = st.selectbox('주거위치는 어디신가여?',['도시','반도시','시골'])
    if Property_Area == '도시' :
        Property_Area = 2
    elif Property_Area == '반도시' :
        Property_Area = 1
    else :
        Property_Area = 0

    if st.button('대출금액 예측') : 
        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,
        Credit_History,Property_Area])
        # 2. 학습할때 사용한 X 의 피처 스케일러를 이용해서, 피처스케일링하기
        # 먼저, 데이터를 2차원으로 만들어준다.

        new_data = new_data.reshape(1, 11)
        new_data = scaler_X.transform(new_data)
        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)
        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = scaler_y.inverse_transform(y_pred)

        # y_pred = [Gender + Married + Dependents + Education  + Self_Employed  + ApplicantIncome  + CoapplicantIncome  + LoanAmount  + Loan_Amount_Term 
        #  + Credit_History  + Property_Area]
        y_pred = round(y_pred[0,0])
        st.write('대출 가능 금액은'+ str(y_pred) + '달러입니다.')










