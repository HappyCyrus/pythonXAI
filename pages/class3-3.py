# while 迴圈
# while 會搭配一個條件來使用
# 條件式為 True 時會一直執行
# 條件式為 False 時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件是否變成　False
i = 0
while i < 5:
    print(i)
    i += 1

# break 可以強制跳出迴圈，先判斷 break　屬於哪個迴圈，然後跳出該迴圈
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

for i in range(5):
    print(i)
    if i == 3:
        break

import random
# random.randrange() 設定抽籤範圍的方法跟 range() 一樣
print(random.randrange(7))   # 0 ~ 6
print(random.randrange(1, 7))   # 1 ~ 6
print(random.randrange(1, 7, 2))   # 1 ~ 6 間隔 2

# random.randint() 設定抽籤範圍的方法一定要設定開始跟結束
# 且結束的數字會包含在內
print(random.randint(1, 6))   # 1 ~ 6