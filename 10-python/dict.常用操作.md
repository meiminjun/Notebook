# dict 常用操作

## 字典合并的几种常用方式

## 方式一



```python
dic1 = { "a":3, "b": "3" }

dic2 = { "c":4, "d": "5", "a": 4 }

dic3 = {}

dic3.update(dic1)
print(dic3)
dic3.update(dic2)
print(dic3)
```

    {'a': 3, 'b': '3'}
    {'a': 4, 'b': '3', 'c': 4, 'd': '5'}



```python
## 方式二
dic1 = {"a": 3, "b": "3"}

dic2 = {"c": 4, "d": "5", "a": 4}

dic3=dict(dic1,**dic2)

print(dic3)
```

    {'a': 4, 'b': '3', 'c': 4, 'd': '5'}


## 方式三（推荐）


```python
dic1 = {"a": 3, "b": "3"}

dic2 = {"c": 4, "d": "5", "a": 4}

dic3 = {**dic1, **dic2}

print(dic3)

```

    {'a': 4, 'b': '3', 'c': 4, 'd': '5'}

