# dataframe 的常见操作


```python
import pandas as pd

df1 = pd.DataFrame({'x1': ["a", "b", "c", "a"], "x2": [
                   "11.2", "23.2", "23.4", "1"], "x3": ["11.2", "23.2", "23.4", "12"]})
print(df1)
df2 = pd.DataFrame({'x1': ["a", "b", "d"], "x2": ["20.23", 'NaN', "90.4"]})
print(df2)

```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
      x1     x2
    0  a  20.23
    1  b    NaN
    2  d   90.4



```python
print(df1)
# df1.loc[:, 'x1'].tolist()[-time]
print(df1.loc[:, 'x1'])
va1 = df1.loc[:, 'x2'].tolist()[-1]
va2 = df1.loc[:, 'x3'].tolist()[-1]

# va3 = va1 - va2
# print(va3)
# print(va2)

```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    0    a
    1    b
    2    c
    Name: x1, dtype: object



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /var/folders/vh/4zv6yqys5w7dry2wxbzxkkvxf0lzcv/T/ipykernel_36514/1791069689.py in <module>
          5 va2 = df1.loc[:, 'x3'].tolist()[-1]
          6 
    ----> 7 va3 = va1 - va2
          8 print(va3)
          9 # print(va2)


    TypeError: unsupported operand type(s) for -: 'str' and 'str'


## 一、索引的最常见操作

### 1、 设置索引


```python
df1.set_index('x1')

# 设置多重索引
print(df1.set_index(['x1', 'x3']))

# drop=False 表示保留原先"YY"列的数据
df1_drop = df1.set_index("x1", drop=False)  
print(df1_drop)

# index索引对象可以转换成列表类型
print(list(df1.index))  # ['ll', 'll', 'mm']

```

               x2
    x1 x3        
    a  11.2  11.2
    b  23.2  23.2
    c  23.4  23.4
       x1    x2    x3
    x1               
    a   a  11.2  11.2
    b   b  23.2  23.2
    c   c  23.4  23.4
    [0, 1, 2]


### 2、 初始设置索引


```python
my_df = pd.DataFrame({
    'Person': ['Alice', 'Steven', 'Neesham', 'Chris', 'Alice'],
    'City': ['Berlin', 'Montreal', 'Toronto', 'Rome', 'Munich'],
    'Mother Tongue': ['German', 'French', 'English', 'Italian', 'German'],
    'Age':  [37, 20, 38, 23, 35],

}, index=["A", "B", "C", "D", "E"])

print(my_df)
```

        Person      City Mother Tongue  Age
    A    Alice    Berlin        German   37
    B   Steven  Montreal        French   20
    C  Neesham   Toronto       English   38
    D    Chris      Rome       Italian   23
    E    Alice    Munich        German   35


### 3、 使用 reset_index() 方法删除 Pandas DataFrame 的索引

参数inplace:
* inplace=True：不创建新的对象，直接对原始对象进行修改；
* inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。

参数drop:
* drop=True: 把原来的索引index列去掉，丢掉。
* drop=False:保留原来的索引（以前的可能是乱的）


```python
my_df = pd.DataFrame({
    'Person': ['Alice', 'Steven', 'Neesham', 'Chris', 'Alice'],
    'City': ['Berlin', 'Montreal', 'Toronto', 'Rome', 'Munich'],
    'Mother Tongue': ['German', 'French', 'English', 'Italian', 'German'],
    'Age':  [37, 20, 38, 23, 35],

}, index=["A", "B", "C", "D", "E"])

df_reset = my_df.reset_index()
# 等同上面
# my_df.reset_index(inplace=True)

print("Before reseting Index:")
print(my_df, "\n")

print("After reseting Index:")
print(df_reset)

```

    Before reseting Index:
        Person      City Mother Tongue  Age
    A    Alice    Berlin        German   37
    B   Steven  Montreal        French   20
    C  Neesham   Toronto       English   38
    D    Chris      Rome       Italian   23
    E    Alice    Munich        German   35 
    
    After reseting Index:
      index   Person      City Mother Tongue  Age
    0     A    Alice    Berlin        German   37
    1     B   Steven  Montreal        French   20
    2     C  Neesham   Toronto       English   38
    3     D    Chris      Rome       Italian   23
    4     E    Alice    Munich        German   35


> 它将重置 DataFrame 的索引，但现在的索引将显示为 index 列。如果我们想删除 index 列，我们可以在 reset_index() 方法中设置 drop=True


```python
my_df = pd.DataFrame({
    'Person': ['Alice', 'Steven', 'Neesham', 'Chris', 'Alice'],
    'City': ['Berlin', 'Montreal', 'Toronto', 'Rome', 'Munich'],
    'Mother Tongue': ['German', 'French', 'English', 'Italian', 'German'],
    'Age':  [37, 20, 38, 23, 35],

},index=["A","B","C","D","E"])

# 重置索引，并且删除原来的索引
df_reset=my_df.reset_index(drop=True)

print("Before reseting Index:")
print(my_df,"\n")

print("After reseting Index:")
print(df_reset)
```

    Before reseting Index:
        Person      City Mother Tongue  Age
    A    Alice    Berlin        German   37
    B   Steven  Montreal        French   20
    C  Neesham   Toronto       English   38
    D    Chris      Rome       Italian   23
    E    Alice    Munich        German   35 
    
    After reseting Index:
        Person      City Mother Tongue  Age
    0    Alice    Berlin        German   37
    1   Steven  Montreal        French   20
    2  Neesham   Toronto       English   38
    3    Chris      Rome       Italian   23
    4    Alice    Munich        German   35


## 二、合并数据


```python
# 以左边列为基准
pd.merge(df1, df2, how='left', on='x1')

# 以右边列为基准
pd.merge(df1, df2, how='right', on='x1')

# 已交集
pd.merge(df1, df2, how='inner', on='x1')

# 全部
pd.merge(df1, df2, how='outer', on='x1')

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
      <th>x1</th>
      <th>x2_x</th>
      <th>x2_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>11.2</td>
      <td>20.23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>23.2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>23.4</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>NaN</td>
      <td>90.4</td>
    </tr>
  </tbody>
</table>
</div>



### concat拼接数据


```python
print(df1)

print(df2)
pd.concat([df1, df2])

```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
      x1     x2
    0  a  20.23
    1  b    NaN
    2  d   90.4





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
      <th>x1</th>
      <th>x2</th>
      <th>x3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>11.2</td>
      <td>11.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>23.2</td>
      <td>23.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>23.4</td>
      <td>23.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>1</td>
      <td>12</td>
    </tr>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>20.23</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>90.4</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## 三、行、列的转置

> 原先的索引变成了行，所以说要转置时，先设置一下索引，不然转换后colums 变成了数字索引


```python
print(df1)
# 
print(df1.T)
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
           0     1     2
    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4


### 正确的方式



```python
print(df1.set_index('x1'))

print('\n 转换后:\n')

print(df1.set_index('x1').T)

```

          x2    x3
    x1            
    a   11.2  11.2
    b   23.2  23.2
    c   23.4  23.4
    
     转换后:
    
    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4


## 四、行列获取

### 1. 列获取

方式一： 按标签（最常用）


```python
print(df1)

print('获取单列')
print(df1['x1'])

print('\n获取多列\n')
print(df1[['x1','x3']])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /var/folders/vh/4zv6yqys5w7dry2wxbzxkkvxf0lzcv/T/ipykernel_36514/533886085.py in <module>
    ----> 1 print(df1)
          2 
          3 print('获取单列')
          4 print(df1['x1'])
          5 


    NameError: name 'df1' is not defined


方式二： 按索引


```python
# 单索引
print(df1.iloc[:, 0])

# 多索引
print(df1.iloc[:, 0:])
```

    0    a
    1    b
    2    c
    Name: x1, dtype: object
      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4


### 2. 行获取

方式一： 按标签获取：


```python
df3 = df1.set_index('x1').T
print(df3)
# 按标签获取
df3.loc['x2']

```

    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4





    x1
    a    11.2
    b    23.2
    c    23.4
    Name: x2, dtype: object



方式二：按索引获取


```python
print('正常获取：')
print(df3.iloc[0])

print('\n区间获取\n')
print(df3.iloc[0:1])

```

    正常获取：
    x1
    a    11.2
    b    23.2
    c    23.4
    Name: x2, dtype: object
    
    区间获取
    
    x1     a     b     c
    x2  11.2  23.2  23.4


### 3. 精准取值


```python
print(df1)

print('方法一：按索引精准取值')
name = df1.iloc[0, 0]  # 获取第一行，指定列数据
print("\n第一行第一列的值：" + name)

print('\n方法二：按标签精准取值\n')
name = df1.loc[0, 'x1']
print(name)
print("\n第一行第一列的值：" + name)
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    方法一：按索引精准取值
    
    第一行第一列的值：a
    
    方法二：按标签精准取值
    
    a


## 五、行列删除

axis=0 : 行删除(默认)

axis=1 : 列删除 


```python
# print(df1)
print(df1)
print('\n 删除行\n')
print(df1.drop(['x1','x3']))

print('\n 删除列数据\n')
print(df1.drop([0], axis=1))

```

           0     1     2
    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4
    
     删除行
    
           0     1     2
    x2  11.2  23.2  23.4
           1     2
    x1     b     c
    x2  23.2  23.4
    x3  23.2  23.4


## 六、列的数据格式化操作

1. 直接列操作


```python
print(df1)

df1['x4'] = df1['x2'] + df1['x3']

print(df1)
```

      x1    x2    x3        x4
    0  a  11.2  11.2  11.211.2
    1  b  23.2  23.2  23.223.2
    2  c  23.4  23.4  23.423.4
      x1    x2    x3        x4
    0  a  11.2  11.2  11.211.2
    1  b  23.2  23.2  23.223.2
    2  c  23.4  23.4  23.423.4


### 2. map方式


```python
# map 方式一
print(df1)

def test(x):
  return f'{x}1'


df1.columns = df1.columns.map(test)
print(df1)


```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
      x11   x21   x31
    0   a  11.2  11.2
    1   b  23.2  23.2
    2   c  23.4  23.4



```python
# map 方式二
df1['x11'] = df1['x11'].map({
  'a': 'a1',
  'b': 'b1',
  'c': 'c1',
})

print(df1)
```

       x11   x21   x31
    0  NaN  11.2  11.2
    1  NaN  23.2  23.2
    2  NaN  23.4  23.4


## 七、行、列名称更改

### 1. 单独更改


```python
print(df1)

print('\n---指定行更改--- \n')

print(df1.rename({ 'x1': 'x11' }))

print('\n---指定行、列更改--- \n')

df1.rename(index={'x2': 'bj'}, columns={
                 0: 11})  # 为某个 index 单独修改名称

```

           0     1     2
    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4
    
    ---指定行更改--- 
    
            0     1     2
    x11     a     b     c
    x2   11.2  23.2  23.4
    x3   11.2  23.2  23.4
    
    ---指定行、列更改--- 
    





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
      <th>11</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>x1</th>
      <td>a</td>
      <td>b</td>
      <td>c</td>
    </tr>
    <tr>
      <th>bj</th>
      <td>11.2</td>
      <td>23.2</td>
      <td>23.4</td>
    </tr>
    <tr>
      <th>x3</th>
      <td>11.2</td>
      <td>23.2</td>
      <td>23.4</td>
    </tr>
  </tbody>
</table>
</div>



### 2. 批量更改


```python
print(df1)

# 自定义map函数
def test_map(x):
    return x+'_ABC'


# print(df1.index.map(test_map))
# 输出 Index(['BEIJING_ABC', 'SHANGHAI_ABC', 'GUANGZHOU_ABC'], dtype='object')

print(df1.rename(index=test_map))

```

           0     1     2
    x1     a     b     c
    x2  11.2  23.2  23.4
    x3  11.2  23.2  23.4
               0     1     2
    x1_ABC     a     b     c
    x2_ABC  11.2  23.2  23.4
    x3_ABC  11.2  23.2  23.4


## 八、去重

```bash
data.drop_duplicates(subset=['A','B'],keep='first',inplace=True)
```

* subset对应的值是列名，表示只考虑这两列，将这两列对应值相同的行进行去重。
默认值为subset=None表示考虑所有列。
* keep='first'表示保留第一次出现的重复行，是默认值。keep另外两个取值为"last"和False，
分别表示保留最后一次出现的重复行和去除所有重复行。
* inplace=True表示直接在原来的DataFrame上删除重复项，而默认值False表示生成一个副本



```python
print(df1)
print('去重')
df1 = df1.drop_duplicates(['x1'])
print(df1)
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    去重
      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4


## 九、累加

```
DataFrame.cumsum(axis=None, skipna=True, *args, **kwargs)
```

* axis	对每行的值累加（1或columns）或者对每列的值累加（0或index）	可选值{0 or ‘index’, 1 or ‘columns’}, 默认值0
* skipna	是否排除空值（NaN）	默认值True
* 返回值	为Series 或 DataFrame



```python
print(df1)

print('行累加')

# 行累加
print(df1.cumsum())

print('列累加')

print(df1.cumsum(axis=1))

```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
    行累加
         x1             x2              x3
    0     a           11.2            11.2
    1    ab       11.223.2        11.223.2
    2   abc   11.223.223.4    11.223.223.4
    3  abca  11.223.223.41  11.223.223.412
    列累加
      x1     x2         x3
    0  a  a11.2  a11.211.2
    1  b  b23.2  b23.223.2
    2  c  c23.4  c23.423.4
    3  a     a1       a112

