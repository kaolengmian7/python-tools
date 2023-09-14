"""
List:有序、重复

"""

# 创建
empty_list = list()
empty_list = []

# 访问，支持正索引和负索引
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0])
print(fruits[-1])

# 访问，支持切片，左闭右开，与 Golang 一致，同样支持负索引
print(fruits[:2])

# 检查某个元素是否存在
exist = 'orange' in fruits
print(exist)

# 查找某个元素的索引
print(fruits.index('orange'))

# 末尾追加新元素
fruits.append('apple')
print(fruits)

# 插入新元素
fruits.insert(1, 'watermelon')
print(fruits)

# 计算某个元素在 List 中的个数
print(fruits.count('orange'))

# 反转列表
# print(fruits.reverse())

# 复制 List
f2 = fruits.copy()
f2[0] = 'GG'
print(fruits)
print(f2)

# List 合并
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print(fruits + vegetables)
print(fruits.extend(vegetables))  # 注意 extend 函数返回值为 None，但是并不意味着 List 合并失败
print(fruits)

print("---------------")

# 删除指定元素，如果不指定索引，删除的是整个 List
del fruits[1]
print(fruits)

# 使用索引删除元素，如果未指定索引，则删除最后一个元素
fruits.pop(1)
print(fruits)

# 使用元素名称删除元素、
fruits.remove('mango')
print(fruits)

# 清空 List
fruits.clear()
print(fruits)

# 排序，如果是字符串就按照首字符顺序排序
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)


nums = [4, 6, 1, 8, 2, 3, 7, 9]
nums.sort(reverse=True)
print(nums)


print(list([1, 2, 3, 4]))
