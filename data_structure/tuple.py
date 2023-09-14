import hashlib

# 创建
empty_tuple = tuple()
empty_tuple = ()

# 支持索引访问，支持切片访问
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[-3:-1])

# 如果需要改变元组，请转换为 List

# 合并
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
print(fruits + vegetables)

# 创建复杂的字段
point_dict = {(0, 0): "Origin", (1, 1): "Point A", (2, 3): "Point B"}
print(point_dict[(0, 0)])  # 输出: Origin

# 用于 hash
data = ("John", "Doe", "1980-01-01")
data_str = str(data)  # 将元组转换为字符串
print(data_str)
data_bytes = data_str.encode()  # 将字符串编码为字节对象
hash_value = hashlib.sha256(data_bytes).hexdigest()
print(hash_value)


# 多个参数的打包
def print_person_info(name, age, address):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)


person = ("John", 30, "123 Main St")
print_person_info(*person)  # 使用元组进行参数解包


# 多返回值
def process_data(data):
    # 处理数据的逻辑...
    processed_data = ...  # 处理后的数据
    summary = ...  # 数据摘要
    return processed_data, summary


input_data = ...  # 输入数据
result, summary = process_data(input_data)  # 函数返回一个元组
print("Processed Data:", result)
print("Summary:", summary)
