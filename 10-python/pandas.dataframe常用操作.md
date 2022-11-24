# dataframe 的常见操作


```python
import pandas as pd

df0 = pd.DataFrame({"x2": [
                   11.2, 23.2, 23.4, 1], "x3": [11.2, 23.2, 23.4, 12]})

print(df0)

df1 = pd.DataFrame({'x1': ["a", "b", "c", "a"], "x2": [
                   "11.2", "23.2", "23.4", "1"], "x3": ["11.2", "23.2", "23.4", "12"]})
print(df1)
df2 = pd.DataFrame({'x1': ["a", "b", "d"], "x2": ["20.23", 'NaN', "90.4"]})
print(df2)

data = {'brand_model': ['德力西 GW912200', '埃帝尔 IB-207TPN-06231C02', '德力西 72LT3YFM40D', '科顺 2-3654-561 铆钉型'],
        'cate': ['低压', '管阀', '低压', '搬运']}
df3 = pd.DataFrame(data)
print(df3)

df5 = pd.DataFrame({'x1': ["12", "23", "99", "123"], "x2": [
                   "11.2", "23.2", "23.4", "1"], "x3": ["11.2", "23.2", "23.4", "12"]})
print(df5)
df6 = pd.DataFrame({'x1': ["12%", "23", "99", "123"], "x2": [
                   "11.2", "23.2%", "23.4", "1"], "x3": ["11.2", "23.2%", "23.4%", "12%"]})

# 判断dataframe数据为空
df7 = pd.DataFrame(data=[], columns=[1,2])
print(df7.empty)

```

         x2    x3
    0  11.2  11.2
    1  23.2  23.2
    2  23.4  23.4
    3   1.0  12.0
      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
      x1     x2
    0  a  20.23
    1  b    NaN
    2  d   90.4
                  brand_model cate
    0            德力西 GW912200   低压
    1  埃帝尔 IB-207TPN-06231C02   管阀
    2         德力西 72LT3YFM40D   低压
    3       科顺 2-3654-561 铆钉型   搬运
        x1    x2    x3
    0   12  11.2  11.2
    1   23  23.2  23.2
    2   99  23.4  23.4
    3  123     1    12
    True



```python
print(df1)
# df1.loc[:, 'x1'].tolist()[-time]
print(df1.loc[:, 'x1'])
va1 = df1.loc[:, 'x2'].tolist()[-1]
va2 = df1.loc[:, 'x3'].tolist()[-1]

va3 = va1 - va2
print(va3)
print(va2)
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
    0    a
    1    b
    2    c
    3    a
    Name: x1, dtype: object



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /var/folders/w6/9k4dzqlj617f06dfby_vk1pr0000gn/T/ipykernel_13699/4084052124.py in <module>
          5 va2 = df1.loc[:, 'x3'].tolist()[-1]
          6 
    ----> 7 va3 = va1 - va2
          8 print(va3)
          9 print(va2)


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
    a  12       1
       x1    x2    x3
    x1               
    a   a  11.2  11.2
    b   b  23.2  23.2
    c   c  23.4  23.4
    a   a     1    12
    [0, 1, 2, 3]


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



### concat拼接数据(类似append)


```python
print(df1)

print(df2)

print('\n 列拼接\n')
print(pd.concat([df1, df2], axis=1))

print('\n 行拼接\n')
pd.concat([df1, df2])

```

      x111222 x211222 x311222
    0       a    11.2    11.2
    1       b    23.2    23.2
    2       c    23.4    23.4
    3       a       1      12
      x1     x2
    0  a  20.23
    1  b    NaN
    2  d   90.4
    
     列拼接
    
      x111222 x211222 x311222   x1     x2
    0       a    11.2    11.2    a  20.23
    1       b    23.2    23.2    b    NaN
    2       c    23.4    23.4    d   90.4
    3       a       1      12  NaN    NaN
    
     行拼接
    





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
      <th>x111222</th>
      <th>x211222</th>
      <th>x311222</th>
      <th>x1</th>
      <th>x2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>11.2</td>
      <td>11.2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>23.2</td>
      <td>23.2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>23.4</td>
      <td>23.4</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a</td>
      <td>1</td>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>a</td>
      <td>20.23</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>b</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>d</td>
      <td>90.4</td>
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

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
    获取单列
    0    a
    1    b
    2    c
    3    a
    Name: x1, dtype: object
    
    获取多列
    
      x1    x3
    0  a  11.2
    1  b  23.2
    2  c  23.4
    3  a    12


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

### 1. 直接列操作


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


def test2(x):
  return f'{x}2'

df1.columns = df1.columns.map(test)
print(df1)

# 匿名函数
df1.columns = df1.columns.map(lambda x: f'{x}222')
print(df1)


```

      x11   x21   x31
    0   a  11.2  11.2
    1   b  23.2  23.2
    2   c  23.4  23.4
    3   a     1    12
      x111  x211  x311
    0    a  11.2  11.2
    1    b  23.2  23.2
    2    c  23.4  23.4
    3    a     1    12
      x111222 x211222 x311222
    0       a    11.2    11.2
    1       b    23.2    23.2
    2       c    23.4    23.4
    3       a       1      12



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


### 3. split 字符串拆分处理

```
split`(*self*, *pat=None*, *n=-1*, *expand=False*)
pat：分列的依据，可以是空格，符号，字符串等等。
n：分列的次数，不指定的话就会根据符号的个数全部分列。
expand：为True可以直接将分列后的结果转换成DataFrame。
如果想要从最右边开始分列，可以使用rsplit()，rsplit()和split()的用法类似，一个从右边开始，一个从左边开始。
```


```python
print(df3)
df4 = df3['brand_model'].str.split(' ', 1, expand=True)


print('\n格式化后：\n')
print(df4)

print('\n 列拼接 \n')
print(pd.concat([df3, df4], axis=1))

```

                  brand_model cate
    0            德力西 GW912200   低压
    1  埃帝尔 IB-207TPN-06231C02   管阀
    2         德力西 72LT3YFM40D   低压
    3       科顺 2-3654-561 铆钉型   搬运
    
    格式化后：
    
         0                   1
    0  德力西            GW912200
    1  埃帝尔  IB-207TPN-06231C02
    2  德力西         72LT3YFM40D
    3   科顺      2-3654-561 铆钉型
    
     列拼接 
    
                  brand_model cate    0                   1
    0            德力西 GW912200   低压  德力西            GW912200
    1  埃帝尔 IB-207TPN-06231C02   管阀  埃帝尔  IB-207TPN-06231C02
    2         德力西 72LT3YFM40D   低压  德力西         72LT3YFM40D
    3       科顺 2-3654-561 铆钉型   搬运   科顺      2-3654-561 铆钉型


### 4. apply、applymap批量更改


```python
print(df0)
print('\n 格式化后\n')
print(df0.apply(lambda x: x+1))

print('\n applymap格式化后\n')

print(df0.applymap(lambda x: x+2))
# 过滤将包含-改为0
df3_0 = df3.applymap(lambda x: 0 if '-' in x else x)
print(df3_0)
# 沿着列轴求和
df0[["x2"]].apply(sum, axis=0)
```

         x2    x3
    0  11.2  11.2
    1  23.2  23.2
    2  23.4  23.4
    3   1.0  12.0
    
     格式化后
    
         x2    x3
    0  12.2  12.2
    1  24.2  24.2
    2  24.4  24.4
    3   2.0  13.0
    
     applymap格式化后
    
         x2    x3
    0  13.2  13.2
    1  25.2  25.2
    2  25.4  25.4
    3   3.0  14.0
           brand_model cate
    0     德力西 GW912200   低压
    1                0   管阀
    2  德力西 72LT3YFM40D   低压
    3                0   搬运





    x2    58.8
    dtype: float64



### 5、类型转换

> 股票代码的补位，例如000123，转成csv或者excel 时，变变成123

```
df['正股代码']  = df['正股代码'].str.zfill(6) #用的时候必须加上.str前缀

<!-- 有时候似乎有问题 -->
df['正股代码'] = df['正股代码'].astype('str') #将原本的int数据类型转换为文本

df.to_csv('./test.csv', dtype = object)

```

### 6、变更类型


```python
dfx4 = pd.DataFrame([['11', '1.2', '3'], ['22', '4.8', '5']], columns=['a', 'b', 'c'])

# dfx4['a'].str.replace('万','').astype('int')
dfx4['b'].astype('int')
dfx4['b'].dtypes
# dfx4['b']
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /var/folders/w6/9k4dzqlj617f06dfby_vk1pr0000gn/T/ipykernel_14591/716864053.py in <module>
          2 
          3 # dfx4['a'].str.replace('万','').astype('int')
    ----> 4 dfx4['b'].astype('int')
          5 dfx4['b'].dtypes
          6 # dfx4['b']


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/generic.py in astype(self, dtype, copy, errors)
       5813         else:
       5814             # else, only a single dtype is given
    -> 5815             new_data = self._mgr.astype(dtype=dtype, copy=copy, errors=errors)
       5816             return self._constructor(new_data).__finalize__(self, method="astype")
       5817 


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/internals/managers.py in astype(self, dtype, copy, errors)
        416 
        417     def astype(self: T, dtype, copy: bool = False, errors: str = "raise") -> T:
    --> 418         return self.apply("astype", dtype=dtype, copy=copy, errors=errors)
        419 
        420     def convert(


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/internals/managers.py in apply(self, f, align_keys, ignore_failures, **kwargs)
        325                     applied = b.apply(f, **kwargs)
        326                 else:
    --> 327                     applied = getattr(b, f)(**kwargs)
        328             except (TypeError, NotImplementedError):
        329                 if not ignore_failures:


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/internals/blocks.py in astype(self, dtype, copy, errors)
        589         values = self.values
        590 
    --> 591         new_values = astype_array_safe(values, dtype, copy=copy, errors=errors)
        592 
        593         new_values = maybe_coerce_values(new_values)


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/dtypes/cast.py in astype_array_safe(values, dtype, copy, errors)
       1307 
       1308     try:
    -> 1309         new_values = astype_array(values, dtype, copy=copy)
       1310     except (ValueError, TypeError):
       1311         # e.g. astype_nansafe can fail on object-dtype of strings


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/dtypes/cast.py in astype_array(values, dtype, copy)
       1255 
       1256     else:
    -> 1257         values = astype_nansafe(values, dtype, copy=copy)
       1258 
       1259     # in pandas we don't store numpy str dtypes, so convert to object


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/core/dtypes/cast.py in astype_nansafe(arr, dtype, copy, skipna)
       1172         # work around NumPy brokenness, #1987
       1173         if np.issubdtype(dtype.type, np.integer):
    -> 1174             return lib.astype_intsafe(arr, dtype)
       1175 
       1176         # if we have a datetime/timedelta array of objects


    /usr/local/anaconda3/envs/py39/lib/python3.9/site-packages/pandas/_libs/lib.pyx in pandas._libs.lib.astype_intsafe()


    ValueError: invalid literal for int() with base 10: '1.2'



```python
dfx3 = pd.DataFrame([['11', '1.2', '3'], ['22', '4.8', '5']], columns=['a', 'b', 'c'])
print(dfx3)
# pd.to_numeric()自动转换成float类型
print(dfx3.apply(pd.to_numeric, errors='ignore', downcast='float'))
print(dfx3.dtypes)
# 遍历的方式格式转换
dfx3.applymap(lambda x: float(x))
# print(dfx3['a'].dtypes)


# df['a'].str.replace('万','').astype('float')
```

        a    b  c
    0  11  1.2  3
    1  22  4.8  5
          a    b    c
    0  11.0  1.2  3.0
    1  22.0  4.8  5.0
    a    object
    b    object
    c    object
    dtype: object





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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11.0</td>
      <td>1.2</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22.0</td>
      <td>4.8</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



### 7、查看列类型


```python
print(dfx3['a'].dtypes)
```

## 七、行、列名称更改

### 1. 单独更改

> 不会更改源数据，要重新赋值


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

# print(df1.rename(index=test_map))
print(df1.rename(index=lambda x: f'{x}%'))

# print(df1['x1'].map(lambda x: f'{x}%'))
# df1['x1'] = df1['x1'].map(lambda x: f'{x}%')
# print(df1)
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a     1    12
       x1    x2    x3
    0%  a  11.2  11.2
    1%  b  23.2  23.2
    2%  c  23.4  23.4
    3%  a     1    12
       x1    x2    x3
    0  a%  11.2  11.2
    1  b%  23.2  23.2
    2  c%  23.4  23.4
    3  a%     1    12


## 批量去除%,并转化为float类型（排序）



```python
print(df6)
df6_out = df6.applymap(lambda x: x if not x.endswith('%') else float(x.replace('%', '')))
print(df6_out)
```

        x1     x2     x3
    0  12%   11.2   11.2
    1   23  23.2%  23.2%
    2   99   23.4  23.4%
    3  123      1    12%
         x1    x2    x3
    0  12.0  11.2  11.2
    1    23  23.2  23.2
    2    99  23.4  23.4
    3   123     1  12.0


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


## 十、排序


```python
print(df5)
# 先转化成number
df5['x1'] = df5['x1'].map(lambda x: float(x))
df5.sort_values(by='x1') # 默认升序
```

          x1    x2    x3
    0   12.0  11.2  11.2
    1   23.0  23.2  23.2
    2   99.0  23.4  23.4
    3  123.0     1    12





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
      <td>12.0</td>
      <td>11.2</td>
      <td>11.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23.0</td>
      <td>23.2</td>
      <td>23.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>99.0</td>
      <td>23.4</td>
      <td>23.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123.0</td>
      <td>1</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



## 删除指定条件的行


```python
print(df5)
# 先转成数字类型
df5= df5.applymap(lambda x: float(x))
# 删除x1列大于20的第一行
print(df5.drop(index=df5[df5['x1'] > 20].index[0]))
# 删除x1列大于20的所有行
print(df5.drop(index=df5[df5['x1'] > 20].index))
```

          x1    x2    x3
    0   12.0  11.2  11.2
    1   23.0  23.2  23.2
    2   99.0  23.4  23.4
    3  123.0   1.0  12.0
          x1    x2    x3
    0   12.0  11.2  11.2
    2   99.0  23.4  23.4
    3  123.0   1.0  12.0
         x1    x2    x3
    0  12.0  11.2  11.2


## dataframe to json


```python
print(df5)

df5.to_json(orient='table')

```

        x1    x2    x3
    0   12  11.2  11.2
    1   23  23.2  23.2
    2   99  23.4  23.4
    3  123     1    12





    '{"schema":{"fields":[{"name":"index","type":"integer"},{"name":"x1","type":"string"},{"name":"x2","type":"string"},{"name":"x3","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":0,"x1":"12","x2":"11.2","x3":"11.2"},{"index":1,"x1":"23","x2":"23.2","x3":"23.2"},{"index":2,"x1":"99","x2":"23.4","x3":"23.4"},{"index":3,"x1":"123","x2":"1","x3":"12"}]}'



## 格式化

### 转换成数字类型


```python
print(df1)
# print(df1['x2'])
df1['x2'] = df1['x2'].apply(pd.to_numeric)
# df = df.apply(pd.to_numeric, errors='ignore', downcast='float')
print('格式化')
print(df1['x2'])
```

      x1    x2    x3
    0  a  11.2  11.2
    1  b  23.2  23.2
    2  c  23.4  23.4
    3  a   1.0    12
    格式化
    0    11.2
    1    23.2
    2    23.4
    3     1.0
    Name: x2, dtype: float64

