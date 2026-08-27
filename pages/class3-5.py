import random
import time
import streamlit as st

ss = st.session_state   # 用來縮寫 session_state 的名字
if "ans" not in ss:
    ss.ans = random.randint(1, 100)
if "max_num" not in ss:
    ss.max_num = 100
if "min_num" not in ss:
    ss.min_num = 1
st.title("Guess the number")
num = st.number_input(f"Guess a number between {ss.min_num} and {ss.max_num}:", step=1)
if st.button("Guess"):
    if num == ss.ans:
        st.balloons()
        st.write("You got it!")
    if num > ss.ans:
        st.write("Too high!")
        if num < ss.max_num:
            ss.max_num = num
    elif num < ss.ans:
        st.write("Too low!")
        if num > ss.min_num:
            ss.min_num = num
    time.sleep(1)
    st.rerun()
