## code 1 
如果不依赖外部库，可以用字典手动实现计数：
```python

arr = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = {}

for word in arr:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)
# 输出: {'apple': 3, 'banana': 2, 'cherry': 1}

```

## code 2 
set 会自动去除重复元素，但会丢失原始顺序：
```python
arr = [3, 1, 2, 2, 3, 4, 5, 5]
unique_arr = list(set(arr))  # 转为列表

print(unique_arr)
# 可能输出（顺序不确定）: [1, 2, 3, 4, 5]
```

