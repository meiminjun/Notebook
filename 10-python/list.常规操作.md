# list 的常用操作

## list转string



```python
LIST = ['1','2','3']
a = '-'.join(LIST)
print(a)
```

    1-2-3


## 元素是否存在于列表中


```python
3 in [1, 2, 3]
```




    True



## 批量替换操作


```python
import re
arr = ['猪肉概念股', '牛肉概念股', '特斯拉概念股']
result = list(map(lambda x: re.sub('概念股', '', x),arr))
print(result)

```

    ['猪肉', '牛肉', '特斯拉']

