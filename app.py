import streamlit as st


def main():
    st.title('대출가능금액 예상해보기')
    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴 선택', menu)
    
    if choice == menu[0] :
        pass
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        pass



if __name__ == '__main__' :
    main() 