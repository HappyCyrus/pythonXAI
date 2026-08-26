import streamlit as st
st.title("數字金字塔")
num = st.number_input("請輸入一個數字(1~9)", min_value=1, max_value=9, step=1)
st.write("數字金字塔:")
for i in range(1, num + 1):
    st.write(str(i) * i)

