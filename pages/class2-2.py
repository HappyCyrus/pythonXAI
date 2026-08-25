import streamlit as st

# st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數。
# min_value=0可以設定最小值為0，max_value=100可以設定最大值為100。 
number = st.number_input("請輸入一個整數：", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁使用markdown語法顯示文字
st.markdown(f"你輸入的整數是：{number}")

st.markdown("---")
st.markdown("### 練習")
score = st.number_input("請輸入你的分數", min_value=0, max_value=100, step=1, value=100)
if score >= 90:
    st.write("你的等級是 A")
elif score >= 80:
    st.write("你的等級是 B")
elif score >= 70:
    st.write("你的等級是 C")
elif score >= 60:
    st.write("你的等級是 D")
else:
    st.write("你的等級是 F")


st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕，使用者可以點擊按鈕
# key是按鈕的識別名稱，可以用來區分不同的按鈕
# 如果使用者點擊按鈕，st.button()會回傳True，否則回傳False
st.button("按我一下", key="button1")
if st.button("按我一下", key="balloon"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
st.markdown("---")