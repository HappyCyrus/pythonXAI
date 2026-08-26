import streamlit as st
st.title("欄位元件")
col1, col2 = st.columns(2)
col1.button('按鈕1', key='btn1')   # 在 col1 中建立一個按鈕類似 st.button('按鈕1')
col1.button('按鈕2', key='btn2')   # 在 col2 中建立一個按鈕類似 st.button('按鈕2')

# 3columns, 可以用比例來設定每個 column 的寬度，將比例放到 list 中
col1, col2, col3 = st.columns([1, 2, 3])
col1.button('按鈕1', key='btn3')   # 在 col1 中建立一個按鈕類似 st.button('按鈕1')
col1.button('按鈕2', key='btn4')   # 在 col2 中建立一個按鈕類似 st.button('按鈕2')
col1.button('按鈕3', key='btn5')   # 在 col3 中建立一個按鈕類似 st.button('按鈕3')

con1, con2 = st.columns([1, 2])
with con1:   # 在 con1 中建立一個 with 裡面的內容
    if st.button('按鈕1', key='btn6'):   # 在 con1 中建立一個按鈕
        st.balloons()   # 在 con1 中建立一個氣球
    st.write('我是 con1')
with con2:   # 在 con2 中建立一個 with 裡面的內容
    if st.button('按鈕2', key='btn7'):   # 在 con2 中建立一個按鈕
        st.balloons()   # 在 con2 中建立一個氣球
    st.write('我是 con2')

st.write("---")
st.write("文字輸入元件")
# st.text_input 指令格式 st.text_input(輸入欄位標題, value="預設顯示文字")
text = st.text_input("請輸入文字", value="預設顯示文字")
st.write(f"你輸入的文字是 {text}")

if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("加1", key="ans2"):
    st.session_state.ans1 += 1
st.write(st.session_state.ans1)

if "apple" not in st.session_state:
    st.session_state.apple = 1

if st.button("重整畫面", key="banana"):
    st.rerun()