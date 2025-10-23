arr = [3, 1, 2, 2, 3, 4, 5, 5]
print(set(arr))
unique_arr = list(set(arr))  # 转为列表

print(unique_arr)
# 可能输出（顺序不确定）: [1, 2, 3, 4, 5]
