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


## 循环操作


```python
# 遍历list
my_list = [1, 2, 3, 4, 5]
for ele in my_list:
    print('ele =', ele)
```

    ele = 1
    ele = 2
    ele = 3
    ele = 4
    ele = 5



```python
# 遍历dict
my_dic = {'python教程':"http://c.biancheng.net/python/",\
          'shell教程':"http://c.biancheng.net/shell/",\
          'java教程':"http://c.biancheng.net/java/"}
for ele in my_dic.items():
    print('ele =', ele)
```

    ele = ('python教程', 'http://c.biancheng.net/python/')
    ele = ('shell教程', 'http://c.biancheng.net/shell/')
    ele = ('java教程', 'http://c.biancheng.net/java/')



```python
# enumerate 遍历
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
  print (i, element)
```

    0 one
    1 two
    2 three



```python
columns = [
                '序号', '股票代码', '股票名称', '价格', '涨幅', '成交额', '总市值',
                'PE', 'PE温度', 'PB', 'PB温度', '5年平均股息率', '股息率',
                '静态股息率', '波动率', '最新年报ROE', '5年平均ROE', '5年营收复合增长', '5年利润复合增长', '5年现金流复合增长', '5年分红率复合增长', '净利同比增长', '有息负债率', '股票质押比例', '行业', '自选'
            ]

print(len(columns))


td = [
    '1', '002110', '三钢闽光 ', '5.250', '-0.38%', '1568.07', '128.71', '7.543',
    '55.13', '0.595', '0.68', '14.019%', '15.467%', '8.495%', '会员', '18.44%',
    '28.00%', '34.76%', '33.84%', '-0.33%', '11.04%', '-83.26%', '28.73%',
    '会员', '长材'
]

print(len(td))
```

    26
    25


## list 拆分（均分）


```python
test_list = ['1','2','3','4','5','6','7','8','9','10']

n=3

output=[test_list[i:i + n] for i in range(0, len(test_list), n)]
print(output)
```

    [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['10']]

