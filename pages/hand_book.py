import streamlit as st

with st.expander("Class1 課堂筆記"):
    st.write(
        """
    
# 🐍 Python 入門筆記

## 1. `print()`：把東西顯示出來

`print()` 就像是告訴電腦：

> 「把這個東西顯示在螢幕上！」

```python
print("Cyrus")
print("7E")
print("Hi!")
```

### 換行 `\n`

`\n` 代表**換到下一行**。

```python
print("Hi!\nI am Cyrus.")
```

結果：

```text
Hi!
I am Cyrus.
```

---

# 2. 註解：寫給人看的文字

註解是寫給我們自己看的，**電腦不會執行它**。

### 單行註解

使用 `#`

```python
# 這是我的第一個 Python 程式
print("Hello")
```

在 VS Code 中，通常可以使用 **Ctrl + ?** 快速加入或取消註解。

### 多行註解

可以使用三個引號：

```python
\"""
這是
多行
註解
\"""
```

---

# 3. Python 的基本資料類型

Python 裡面的資料有不同種類。

| 類型      | 名稱      | 例子             |
| ------- | ------- | -------------- |
| `int`   | 整數      | `1`、`0`、`-5`   |
| `float` | 小數      | `1.0`、`3.14`   |
| `str`   | 字串（文字）  | `"apple"`      |
| `bool`  | 布林值（真假） | `True`、`False` |

例如：

```python
print(10)        # int
print(3.14)      # float
print("apple")   # str
print(True)      # bool
```

### ⭐ 小提醒

`"10"` 和 `10` 不一樣！

```python
10
```

是數字。

```python
"10"
```

是文字。

---

# 4. 變數：幫資料取名字

變數可以想像成一個**有名字的盒子**。

```python
a = 10
```

意思就是：

> 做一個叫 `a` 的盒子，把 `10` 放進去。

所以：

```python
print(a)
```

會得到：

```text
10
```

### 變數裡面的東西可以改變

```python
a = 10
print(a)

a = "apple"
print(a)
```

結果：

```text
10
apple
```

所以變數就像一個**可以重新放東西的盒子**。

---

# 5. `=` 是什麼意思？

在 Python 裡：

```python
a = 10
```

不是「a 等於 10」這麼簡單。

它比較像：

> **把右邊的東西放進左邊的變數。**

所以：

```python
a = 10
```

就是把 `10` 存進 `a`。

---

# 6. Python 的數學運算

Python 可以直接算數學！

| 符號   | 意思  | 例子       |
| ---- | --- | -------- |
| `+`  | 加   | `5 + 2`  |
| `-`  | 減   | `5 - 2`  |
| `*`  | 乘   | `5 * 2`  |
| `/`  | 除   | `5 / 2`  |
| `//` | 取商  | `5 // 2` |
| `%`  | 取餘數 | `5 % 2`  |
| `**` | 次方  | `5 ** 2` |

例如：

```python
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)
```

### ⭐ `//` 和 `%` 很容易搞混

假設：

```python
print(7 // 3)
print(7 % 3)
```

`7 ÷ 3`：

* 商是 `2`
* 餘數是 `1`

所以：

```text
7 // 3 → 2
7 % 3  → 1
```

---

# 7. 運算順序

如果一個算式裡有很多運算，Python 有自己的順序。

從先到後：

### ① `()`

括號

### ② `**`

次方

### ③ `* / // %`

乘、除、取商、取餘數

### ④ `+ -`

加、減

例如：

```python
print(2 + 3 * 4)
```

不是 `20`，而是：

```text
14
```

因為先算：

```text
3 × 4 = 12
```

再算：

```text
2 + 12 = 14
```

---

# 8. 字串也可以使用 `+` 和 `*`

字串就是文字。

### `+`：把文字接在一起

```python
print("apple" + "pen")
```

結果：

```text
applepen
```

### `*`：重複文字

```python
print("apple" * 3)
```

結果：

```text
appleappleapple
```

⭐ 注意：

```python
"apple" + "pen"
```

是文字相加，不是數學加法。

---

# 9. f-string：把變數放進文字裡

如果想把變數放進一句話裡，可以使用 `f""`。

例如：

```python
num = 30
item = "book"

print(f"{num}$ per {item}")
```

結果：

```text
30$ per book
```

`{}` 裡面放的是**變數**。

再例如：

```python
name = "Cyrus"
age = 12

print(f"Hello, my name is {name}, I'm {age} years old.")
```

Python 會把 `{name}` 和 `{age}` 換成變數裡面的內容。

---

# 10. `len()`：數一數有幾個字

`len()` 可以計算字串有多長。

```python
print(len("apple"))
```

結果：

```text
5
```

因為：

```text
a p p l e
1 2 3 4 5
```

例如：

```python
print(len("Hello"))
```

結果也是：

```text
5
```

⭐ `len()` 可以想成：

> 「幫我數一下裡面有幾個東西！」

---

# 11. `type()`：查看資料是什麼類型

`type()` 可以問 Python：

> 「這個東西到底是什麼種類？」

例如：

```python
print(type(1))
```

會看到：

```text
<class 'int'>
```

其他例子：

```python
print(type(1.0))
print(type("apple"))
print(type(True))
```

分別是：

```text
float
str
bool
```

---

# 12. 型態轉換

有時候我們需要把資料從一種類型變成另一種類型。

這就叫做**型態轉換**。

## `int()` → 整數

```python
print(int(1.0))
```

結果：

```text
1
```

⚠️ 小數轉整數時，小數部分會被去掉：

```python
print(int(1.234))
```

結果：

```text
1
```

---

## `float()` → 小數

```python
print(float(1))
```

結果：

```text
1.0
```

也可以把數字文字變成小數：

```python
print(float("1.234"))
```

---

## `str()` → 字串

```python
print(str(123))
```

會把數字 `123` 變成文字 `"123"`。

---

## `bool()` → True / False

```python
print(bool(1))
```

會得到：

```text
True
```

---

### ⭐ 型態轉換快速記憶

```text
int()   → 整數
float() → 小數
str()   → 文字
bool()  → True / False
```

---

# 13. `input()`：讓使用者輸入東西

`input()` 可以讓使用者在程式執行時輸入資料。

```python
name = input("請輸入你的名字: ")
```

電腦會顯示：

```text
請輸入你的名字:
```

然後等待使用者輸入。

### ⭐ 非常重要

`input()` **預設會把使用者輸入的東西當成字串 `str`**。

例如：

```python
a = input("請輸入一些文字: ")
print(type(a))
```

即使你輸入：

```text
123
```

它還是會是：

```text
str
```

而不是 `int`。

---

# 14. `input()` + 型態轉換

如果希望使用者輸入數字，就可以自己轉換。

例如：

```python
radius = input("請輸入半徑: ")

print(float(radius) * float(radius) * 3.14)
```

因為 `input()` 得到的是文字，所以先使用：

```python
float(radius)
```

把它變成小數。

這樣就可以拿來做數學運算。

---

# 15. Streamlit：讓 Python 做出網頁

前面的 Python 大多是在**終端機**裡看到結果。

`Streamlit` 可以讓我們把 Python 程式做成比較漂亮的**網頁介面**。

首先：

```python
import streamlit as st
```

意思是：

> 把 Streamlit 工具叫進來，並且幫它取名字叫 `st`。

---

# 16. `st.title()`：網頁的大標題

```python
st.title("這是標題")
```

會在網頁上顯示一個很大的標題。

可以想成：

> 「請幫我做一個大標題！」

---

# 17. `st.write()`：顯示東西

```python
st.write("Hello!")
```

可以在網頁上顯示內容。

它很方便，可以顯示很多不同種類的資料。

---

# 18. `st.text()`：顯示普通文字

```python
st.text("Hello!")
```

就是單純顯示文字。

可以想成：

> `st.text()` = 「把這些文字原原本本顯示出來。」

---

# 19. `st.markdown()`：讓文字變漂亮

`st.markdown()` 可以使用 Markdown 語法，讓網頁文字有不同的效果。

例如：

### 粗體

```markdown
**粗體**
```

### 斜體

```markdown
*斜體*
```

### 標題

```markdown
# 最大標題
## 第二大標題
### 第三大標題
```

數字越多，標題通常越小：

```text
#       最大
##      
###
####
#####
######  最小
```

---

# 20. Markdown 的項目符號

可以使用 `-` 製作清單：

```markdown
- 第一個項目
- 第二個項目
- 第三個項目
```

網頁上會變成：

* 第一個項目
* 第二個項目
* 第三個項目

---

# 21. Markdown 的程式碼區塊

可以使用三個反引號：

````markdown
```python
print("Hello World!")
```
````

這樣就可以在網頁上顯示漂亮的程式碼區塊。

---

# 🎯 今天最重要的指令整理

| 指令 / 符號         | 功能                    |
| --------------- | --------------------- |
| `print()`       | 在螢幕顯示東西               |
| `\n`            | 換行                    |
| `#`             | 單行註解                  |
| `\""" \"""`       | 多行註解                  |
| `=`             | 把右邊的資料放進左邊            |
| `len()`         | 計算長度                  |
| `type()`        | 查看資料類型                |
| `int()`         | 轉成整數                  |
| `float()`       | 轉成小數                  |
| `str()`         | 轉成字串                  |
| `bool()`        | 轉成布林值                 |
| `input()`       | 讓使用者輸入                |
| `import`        | 把工具叫進來                |
| `st.title()`    | Streamlit 大標題         |
| `st.write()`    | Streamlit 顯示內容        |
| `st.text()`     | Streamlit 顯示純文字       |
| `st.markdown()` | Streamlit 顯示 Markdown |

## 🧠 超級簡單版記憶法

```text
print     → 顯示
input     → 輸入
len       → 數長度
type      → 看類型
int       → 整數
float     → 小數
str       → 文字
bool      → 真 / 假
=         → 存東西
+ - * /   → 算數學
st.title  → 網頁大標題
st.write  → 網頁顯示
st.text   → 網頁文字
st.markdown → 網頁漂亮文字
```

    """)
with st.expander("Class2 課堂筆記"):
    st.write(
        """
# 🐍 Python 第二堂課筆記：比較、邏輯與判斷

今天學的內容比上一堂更進一步！我們開始讓 Python **「做決定」**。

可以把 Python 想像成一個很聰明的機器人：

> 「如果這件事情是真的，就做 A；如果不是，就做 B！」

---

## 1. 🔍 比較運算子

比較運算子就是拿兩個東西來**比一比**。

比較之後，答案只會有兩種：

* `True` → **是真的**
* `False` → **是假的**

### 常見的比較符號

| 符號   | 意思    | 例子       | 結果      |
| ---- | ----- | -------- | ------- |
| `==` | 等於    | `1 == 1` | `True`  |
| `!=` | 不等於   | `1 != 1` | `False` |
| `>`  | 大於    | `2 > 1`  | `True`  |
| `<`  | 小於    | `1 < 2`  | `True`  |
| `>=` | 大於或等於 | `2 >= 2` | `True`  |
| `<=` | 小於或等於 | `1 <= 2` | `True`  |

例如：

```python
print(1 == 1)
```

結果：

```text
True
```

因為 `1` 確實等於 `1`。

### ⚠️ `=` 和 `==` 不一樣！

這個非常重要！

```python
a = 10
```

`=` 是把資料**放進變數**。

而：

```python
a == 10
```

`==` 是在問：

> 「a 裡面的東西是不是等於 10？」

---

# 2. 🧠 邏輯運算子

邏輯運算子可以把很多個「True / False」組合起來。

主要有三個：

```text
and
or
not
```

---

## 3. `and`：而且、兩個都要

`and` 的意思可以想成：

> 「這個**而且**那個，都必須是真的！」

只要有一個是 `False`，最後就是 `False`。

| 第一個   | 第二個   | 結果      |
| ----- | ----- | ------- |
| True  | True  | ✅ True  |
| True  | False | ❌ False |
| False | True  | ❌ False |
| False | False | ❌ False |

例如：

```python
print(True and True)
```

結果：

```text
True
```

因為兩個都是 `True`。

### 🌟 生活中的例子

假設：

> 「我有完成作業 **而且** 我有帶課本，才能進教室。」

兩件事情都要做到才可以。

---

# 4. `or`：或者、至少一個

`or` 的意思是：

> 「只要其中一個是真的，就可以！」

| 第一個   | 第二個   | 結果      |
| ----- | ----- | ------- |
| True  | True  | ✅ True  |
| True  | False | ✅ True  |
| False | True  | ✅ True  |
| False | False | ❌ False |

例如：

```python
print(True or False)
```

結果：

```text
True
```

因為至少有一個 `True`。

### 🌟 生活中的例子

> 「今天可以帶雨傘 **或** 穿雨衣。」

只要做到其中一個就可以。

---

# 5. `not`：反過來！

`not` 可以把答案反過來。

```python
print(not True)
```

結果：

```text
False
```

而：

```python
print(not False)
```

結果：

```text
True
```

可以記成：

```text
not True  → False
not False → True
```

### 🧠 超簡單記法

```text
and → 而且 → 全部都要 True
or  → 或者 → 一個 True 就可以
not → 相反 → True 變 False，False 變 True
```

---

# 6. 🚪 `if`：如果……

`if` 是 Python 裡非常重要的指令。

`if` 的意思就是：

> **「如果這個條件是真的，就做這件事。」**

例如：

```python
age = 12

if age >= 10:
    print("你已經十歲以上了！")
```

因為 `12 >= 10` 是 `True`，所以 Python 就會執行 `print()`。

---

# 7. `elif`：不然如果……

`elif` 是：

> **else if → 不然如果**

可以用來檢查下一個條件。

例如：

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
```

因為 `85` 沒有大於等於 `90`，所以第一個 `if` 不成立。

接著 Python 檢查 `elif`：

```text
85 >= 80
```

成立！

所以顯示：

```text
B
```

---

# 8. `else`：不然……

`else` 可以理解成：

> **「上面的條件都不符合，那就做這件事。」**

例如：

```python
score = 50

if score >= 60:
    print("及格")
else:
    print("不及格")
```

因為 `50 >= 60` 是 `False`，所以執行 `else`。

結果：

```text
不及格
```

---

# 9. ⭐ `if`、`elif`、`else` 一起使用

最常見的結構：

```python
if 條件1:
    做事情1
elif 條件2:
    做事情2
else:
    做其他事情
```

可以想成：

```text
        條件1？
       ↙      ↘
     是        不是
     ↓          ↓
   做1        條件2？
             ↙    ↘
           是      不是
           ↓        ↓
         做2      做其他
```

---

# 10. 🔐 密碼門檢查

你今天寫了一個很有趣的程式！

```python
password = input("請輸入密碼：")

if password == "0322":
    print("Welcome home, Cyrus!")
elif password == "0430":
    print("Welcome home, Jayde!")
else:
    print("密碼錯誤，請再試一次。")
```

它的意思是：

### 如果：

密碼是 `"0322"`

➡️ 顯示 Cyrus 歡迎訊息。

### 不然如果：

密碼是 `"0430"`

➡️ 顯示 Jayde 歡迎訊息。

### 不然：

➡️ 顯示「密碼錯誤」。

---

# 11. 🤔 多個 `if` 和 `if + elif + else` 的差別

這是一個很重要的觀念。

### 多個 `if`

```python
if 條件1:
    做事情1

if 條件2:
    做事情2

if 條件3:
    做事情3
```

Python 會**一個一個全部檢查**。

---

### `if + elif + else`

```python
if 條件1:
    做事情1
elif 條件2:
    做事情2
elif 條件3:
    做事情3
else:
    做其他事情
```

當 Python 找到符合的條件後，就會選擇其中一個分支。

所以如果這些條件是「很多個選一個」，通常用 `if + elif + else` 會比較適合，也比較清楚。

---

# 12. 🌐 Streamlit：輸入數字

今天也學了新的 Streamlit 指令：

```python
st.number_input()
```

它可以在網頁上讓使用者輸入**數字**。

例如：

```python
number = st.number_input(
    "請輸入一個整數：",
    step=1,
    min_value=0,
    max_value=100
)
```

這裡有幾個重要設定：

| 設定              | 意思        |
| --------------- | --------- |
| `step=1`        | 每次增加或減少 1 |
| `min_value=0`   | 最小值是 0    |
| `max_value=100` | 最大值是 100  |

所以使用者可以輸入：

```text
0 ～ 100
```

範圍內的整數。

---

# 13. 📝 `st.markdown()`

之前已經學過 `st.markdown()`。

今天再用它來顯示文字：

```python
st.markdown(f"你輸入的整數是：{number}")
```

這裡又用到了之前學的 **f-string**！

`{number}` 會被換成使用者輸入的數字。

---

# 14. 🏆 分數判斷

今天的練習非常重要：

```python
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
```

這就是一個**成績分級系統**。

|     分數 |  等級 |
| -----: | :-: |
| 90～100 |  A  |
|  80～89 |  B  |
|  70～79 |  C  |
|  60～69 |  D  |
|   0～59 |  F  |

Python 會從上面開始一個一個檢查。

例如分數是 `85`：

```text
85 >= 90 ❌
85 >= 80 ✅
```

所以得到：

```text
B
```

---

# 15. 🔘 `st.button()`：做一個按鈕

`st.button()` 可以在網頁上放一個按鈕。

```python
st.button("按我一下")
```

網頁上就會出現一個按鈕：

**按我一下**

---

# 16. `st.button()` 會得到 True 或 False

這個非常重要！

```python
if st.button("按我一下"):
    st.balloons()
```

如果使用者**有按按鈕**：

```text
st.button() → True
```

所以：

```python
if True:
```

就會執行：

```python
st.balloons()
```

如果沒有按：

```text
st.button() → False
```

就不會執行。

---

# 17. 🎈 `st.balloons()`

```python
st.balloons()
```

會在 Streamlit 網頁上出現**氣球動畫** 🎈

例如：

```python
if st.button("按我一下"):
    st.balloons()
```

按下按鈕：

🎈🎈🎈 氣球出現！

---

# 18. ❄️ `st.snow()`

```python
st.snow()
```

會在網頁上出現**下雪效果**。

例如：

```python
if st.button("按我一下"):
    st.snow()
```

按下按鈕：

❄️❄️❄️ 開始下雪！

---

# 19. 🏷️ `key` 是什麼？

如果有很多個按鈕，最好幫它們取不同的 `key`。

例如：

```python
st.button("按我一下", key="balloon")
st.button("按我一下", key="snow")
```

雖然兩個按鈕的文字一樣，但是：

```text
第一個 → balloon
第二個 → snow
```

所以 Python 可以知道：

> 「這是不同的按鈕！」

可以把 `key` 想成按鈕的**身分證號碼**。

---

# 🧠 今天的超級重點

如果要把今天的內容濃縮成最重要的幾句話：

```text
==   → 是不是一樣？
!=   → 是不是不一樣？
>    → 大於
<    → 小於
>=   → 大於或等於
<=   → 小於或等於

and  → 而且，全部都要 True
or   → 或者，一個 True 就可以
not  → 相反

if   → 如果
elif → 不然如果
else → 不然

st.number_input() → 讓使用者輸入數字
st.button()       → 做一個按鈕
st.balloons()     → 氣球效果 🎈
st.snow()         → 下雪效果 ❄️
key               → 給元件一個身分名稱
```

## 🎮 最後用「遊戲」來記住它

你可以把今天學的東西想成一個遊戲：

> 🎮 **玩家輸入分數 → Python 比較分數 → Python 做出判斷 → 顯示結果**

例如：

```text
玩家輸入 95
      ↓
score >= 90？
      ↓
    是！✅
      ↓
顯示「A」
```

所以今天最重要的新觀念就是：

# **「讓 Python 自己做決定！」** 🤖🐍

    """)
with st.expander("Class3 課堂筆記"):
    st.write(
        """

    """)
with st.expander("Class4 課堂筆記"):
    st.write(
        """

    """)
with st.expander("Class5 課堂筆記"):
    st.write(
        """

    """)