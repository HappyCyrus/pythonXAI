print("Cyrus")
print("7E")
print("Hi!\nI am Cyrus.")

"""
這
是
多
行
註
解
"""
# 這是單行註解
# Ctrl+?可以快速註解

# Standerd type
print(1)   # int: -1, 0, 1, 2
print(1.0)   # float
print(1.234)   # float
print("apple")   # str
print(True)   # bool
print(False)   # bool

# variable
a = 10   # 新增一個儲存空間並取名為a。 "="的功能是將右邊的值10儲存在左邊的a
print(a)   # 在終端機顯示a所存的值。
a = "apple"  # 將a的值改為"apple"
print(a)   # 在終端機顯示a所存的值寫好了

# 運算子
print(1 + 1)   # 加法
print(1 - 1)   # 減法
print(1 * 1)   # 乘法
print(1 / 1)   # 除法
print(1 // 1)   # 取商
print(1 % 1)   # 取餘數
print(1 ** 1)   # 次方

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# 字串運輸電腦，+、*
print("apple" + "pen")   # 字串相加
print("apple" * 3)   # 字串乘法

num = 30
item = "book"
print(f"{num}$ per {item}")

name = "Cyrus"
age = 12
print(f"Hello, my name is {name}, I'm {age} years old.")

print(len("apple"))   # len()是一個函式，可以計算字串的長度
print(len(","))   # len()是一個函式，可以計算字串的長度
# type()   可以查看變數的形態
print(type(1))   # <class 'int'>
print(type(1.0))   # <class 'float'>
print(type("apple"))   # <class 'str'>
print(type(True))   # <class 'bool'>

# 型態轉換
print(int(1.0))   # float轉int
print(float(1))   # int轉float
print(str(1))   # int轉str
print(bool(1))   # int轉bool
print(int(1.234))   # float轉int
print(float("1.234"))   # str轉float
print(str(1.234))   # float轉str
print(bool(1.234))   # float轉bool
# print(int("hello"))   # 這行會報錯，因為字串裡面如果有非數字的字元，無法轉換為整數