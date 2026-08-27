# 字典
# dict 是透過 key-value 的方式來儲存資料，key 是唯一的，value 可以重複
# dict 是無序的，所以無法透過 index 來取得資料
# dict 的 key 必須是不可變的資料型態，例如: int, float, string
# dict 的 value 可以是任意資料型態
# dict 的 key-value 是透過冒號來連接，key:value
# dict 的 key-value 是透過逗號來連接
d = {'a': 1, 'b': 2, 'c': 3}

# 取得 dict 的 key
print(d.keys())   # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)

# 取得 dict 的 key
print(d.values())   # dict_values([1, 2, 3])
for value in d.values():
    print(value)

# 取得 dict 的 key-value
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)

# 新增/修改 dict 的 key-value
d['d'] = 4   # 新增
print(d)   # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d['a'] = 5   # 修改
print(d)   # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# 刪除 dict 的 key-value, pop() 方法
# 如果資料有存在，就刪除並回傳 value
print(d.pop('a'))   # 5
# 如果資料沒有存在，就回傳預設值
print(d.pop('e', "Not found"))   # Not found
# 如果資料不存在也沒有預設值，就會報錯

# 檢查 dict 是否有某個 key
# in 不能檢查 value
# 跟 list 比較，in 可以檢查的是 list 的元素與 dict 的 key
print('a' in d)   # True
print('e' in d)   # False

print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
print([1, True, "a", 1.23])  # 這是一個有四個元素的list

# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"

# list 取長度，也就是list中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])

for i in L:
    print(i)


# list的append
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print(L)

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個"a"
# 代表remove會從頭開始找，找到第一個符合的元素就會移除
# 如果想要移除所有符合的元素，可以使用迴圈
for i in L:
    if i == "a":
        L.remove(i)


# 2. 使用pop，可以移除指定的index的元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index的元素
# 如果不指定index，則會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)

# sort：將 List 中的元素進行排序，預設是由小到大（升序排列）
# 注意：這個方法會直接修改原本的 List，不會產生新的 List
L = [1, 3, 2, 4, 5]
L.sort()
print(L)

