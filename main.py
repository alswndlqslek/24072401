import streamlit as st

st.title('my first streamlit app')

name = st.text_input('이름을 입력하세요:')

menu = st.selectbox('좋아하는 음식을 선택하세요:', ['젤리', '마시맬로우', '탕후루', '사탕'])

if st.button('인사말 생성') :
    st.write(f'안녕하세요, {name}님! 당신의 좋아하는 음식은 {menu}입니다. 맛있게먹으세요!')
