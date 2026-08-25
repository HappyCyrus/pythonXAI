# 比較運算子，只能存同樣類型做比較
print(1 == 1)   # True
print(1 != 1)   # False
print(1 > 1)    # False
print(1 < 1)    # False
print(1 >= 1)   # True
print(1 <= 1)   # True

# 邏輯運算子
# and 運算子，只要一個條件為False，結果就是False
print(True and True)     # True
print(True and False)    # False
print(False and True)    # False
print(False and False)   # False

# or 運算子，只要一個條件為True，結果就是True
print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

# not 運算子
print(not True)   # False
print(not False)  # True

# 密碼門檢查
password = input("請輸入密碼：")
if password == "0322":
    print("Welcome home, Cyrus!")
elif password == "0430":
    print("Welcome home, Jayde!")
else:
    print("密碼錯誤，請再試一次。")
# 連續使用if和使用if elif else的差別
# elif 可以排除前面有判斷過的條件，所以縮短判斷條件的復雜度，也節省了時間
# 但是如果是使用多個if，則每個if都會被執行，所以效率較低