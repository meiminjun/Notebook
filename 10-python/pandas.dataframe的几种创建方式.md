# dataframe的几种创建方式


```python
import pandas as pd
```

## 字典创建


```python

dic1 = {"name": ["小明", "小红", "小孙"],
        "age": [20, 18, 27],
        "sex": ["男", "女", "男"]
        }
pd.DataFrame(dic1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>小明</td>
      <td>20</td>
      <td>男</td>
    </tr>
    <tr>
      <td>1</td>
      <td>小红</td>
      <td>18</td>
      <td>女</td>
    </tr>
    <tr>
      <td>2</td>
      <td>小孙</td>
      <td>27</td>
      <td>男</td>
    </tr>
  </tbody>
</table>
</div>



## json 创建


```python
json_arr = [
  {
  "name": "京基智农",
  "no": "000048",
  "url": "http://stock.jrj.com.cn/share,000048.shtml",
  "price": 17.7,
  "up_or_down": "-0.39%",
  "num_ratio": 0.76,
  "change_ratio": "0.08%",
  "pe": 8.6
  },
  {
  "name": "广弘控股",
  "no": "000529",
  "url": "http://stock.jrj.com.cn/share,000529.shtml",
  "price": 6.34,
  "up_or_down": "0.32%",
  "num_ratio": 1.64,
  "change_ratio": "0.45%",
  "pe": 12.24
  },
  {
  "name": "龙大美食",
  "no": "002726",
  "url": "http://stock.jrj.com.cn/share,002726.shtml",
  "price": 10.95,
  "up_or_down": "2.05%",
  "num_ratio": 1.37,
  "change_ratio": "0.8%",
  "pe": 19.07
  }
]

pd.DataFrame(json_arr)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>no</th>
      <th>url</th>
      <th>price</th>
      <th>up_or_down</th>
      <th>num_ratio</th>
      <th>change_ratio</th>
      <th>pe</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>京基智农</td>
      <td>000048</td>
      <td>http://stock.jrj.com.cn/share,000048.shtml</td>
      <td>17.70</td>
      <td>-0.39%</td>
      <td>0.76</td>
      <td>0.08%</td>
      <td>8.60</td>
    </tr>
    <tr>
      <th>1</th>
      <td>广弘控股</td>
      <td>000529</td>
      <td>http://stock.jrj.com.cn/share,000529.shtml</td>
      <td>6.34</td>
      <td>0.32%</td>
      <td>1.64</td>
      <td>0.45%</td>
      <td>12.24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>龙大美食</td>
      <td>002726</td>
      <td>http://stock.jrj.com.cn/share,002726.shtml</td>
      <td>10.95</td>
      <td>2.05%</td>
      <td>1.37</td>
      <td>0.8%</td>
      <td>19.07</td>
    </tr>
  </tbody>
</table>
</div>



> 与下面的Series类似

## 嵌套字典创建


```python
dic2 = {'数量': {'苹果': 3, '梨': 2, '草莓': 5},
        '价格': {'苹果': 10, '梨': 9, '草莓': 8},
        '产地': {'苹果': '陕西', '梨': '山东', '草莓': '广东'}
        }
pd.DataFrame(dic2)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>数量</th>
      <th>价格</th>
      <th>产地</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>苹果</td>
      <td>3</td>
      <td>10</td>
      <td>陕西</td>
    </tr>
    <tr>
      <td>梨</td>
      <td>2</td>
      <td>9</td>
      <td>山东</td>
    </tr>
    <tr>
      <td>草莓</td>
      <td>5</td>
      <td>8</td>
      <td>广东</td>
    </tr>
  </tbody>
</table>
</div>



## 列表创建


```python
lst = ['小明','小红', '小黄']
df1 = pd.DataFrame(lst, columns=["姓名"])
print(df1)
# 修改索引
# df2 = pd.DataFrame(lst, columns=["姓名"], index=[1,2,3])
# print(df2)
```

       姓名
    0  小明
    1  小红
    2  小黄


## 列表嵌套创建


```python

lst = [["小明", "20", "男"],
       ["小红", "23", "女"],
       ["小周", "19", "男"],
       ["小孙", "28", "男"]
       ]
pd.DataFrame(lst, columns=["姓名", "年龄", "性别"])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
      <th>年龄</th>
      <th>性别</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>小明</td>
      <td>20</td>
      <td>男</td>
    </tr>
    <tr>
      <td>1</td>
      <td>小红</td>
      <td>23</td>
      <td>女</td>
    </tr>
    <tr>
      <td>2</td>
      <td>小周</td>
      <td>19</td>
      <td>男</td>
    </tr>
    <tr>
      <td>3</td>
      <td>小孙</td>
      <td>28</td>
      <td>男</td>
    </tr>
  </tbody>
</table>
</div>



## 元组创建


```python
tup = ("小明", "小红", "小周", "小孙")
df12 = pd.DataFrame(tup, columns=["姓名"])
print(df12)
```

       姓名
    0  小明
    1  小红
    2  小周
    3  小孙



```python
tup2 = [("小孙", "男", "12", "1991-03-13"), ("小明", "男", "12", "1991-03-13"), ("小红", "男", "12", "1991-03-13")]
pd.DataFrame(tup2, columns=["姓名", "性别", "年龄", "出生日期"])

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>姓名</th>
      <th>性别</th>
      <th>年龄</th>
      <th>出生日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>小孙</td>
      <td>男</td>
      <td>12</td>
      <td>1991-03-13</td>
    </tr>
    <tr>
      <td>1</td>
      <td>小明</td>
      <td>男</td>
      <td>12</td>
      <td>1991-03-13</td>
    </tr>
    <tr>
      <td>2</td>
      <td>小红</td>
      <td>男</td>
      <td>12</td>
      <td>1991-03-13</td>
    </tr>
  </tbody>
</table>
</div>



> 这种方式与从mysql中提取创建方式类似，
> 区别在于mysql 返回的是元组


## 使用 Series 创建


```python
series = {'水果': pd.Series(['苹果', '梨', '草莓']),
'数量': pd.Series([60, 50, 100]),
'价格': pd.Series([7, 5, 18])}

pd.DataFrame(series)

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>水果</th>
      <th>数量</th>
      <th>价格</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>苹果</td>
      <td>60</td>
      <td>7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>梨</td>
      <td>50</td>
      <td>5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>草莓</td>
      <td>100</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>



## 参考文献

`https://mp.weixin.qq.com/s?src=11&timestamp=1630639469&ver=3291&signature=2hP6UP*xyIiph4dVB7QKEtEbmKdsacG8sFuoIeSYBuRFZ*tDDJPxkb21KefUeBiw7chpJcCW-FnbOtMcfvdy*QpOpjHZzjK0yZFnTKiCPvpn4Cy3H2imaKiJna0nM2J3&new=1`

