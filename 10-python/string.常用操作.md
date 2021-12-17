# 字符串的常用操作

## 判断字符串包含的几种方法


### 1. 成员操作符in



```python
s = '600309-万华化学-指标表'

if '600309' in s:
  print('exist')
else:
  print('no exist')
```

    exist


### 2. find / rfinde 方法

* find: 查找指定值的第一次出现
* rfind: 查找指定值的最后一次出现

如果找不到该值，则 find()/rfind() 方法将返回 -1


```python
s = '600309-万华化学-指标表'

result = s.find('指标表')
print(result)

s.rfind('指标表')

```

    -1





    12



### 3. index/rindex 方法

> 与find 、rfind方法相同，区别是没找到时报错


```python
s = '600309-万华化学-指标表'

result = s.index('指标表1')
print(result)

s.rindex('指标表')

```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-23a22a0113c3> in <module>
          1 s = '600309-万华化学-指标表'
          2 
    ----> 3 result = s.index('指标表1')
          4 print(result)
          5 


    ValueError: substring not found


### 4. startswith 判断以X开头

> str.startswith(str, beg=0,end=len(string));

1. str -- 检测的字符串。
2. strbeg -- 可选参数用于设置字符串检测的起始位置。
3. strend -- 可选参数用于设置字符串检测的结束位置。


```python
"600001".startswith('6')

def format_str(s):
  if s.startswith('6'):
    return f'{s}.SH'
  else:
    return f'{s}.SZ'

format_str('600002') 
format_str('000006') 
```




    '000006.SZ'



## 拼接方法（推荐）



```python
a = "2323"

b = "cdsdc"

c = f'{a}-{b}'

print(c)
```

    2323-cdsdc


## list to string


```python
line = "ddf,dfdf,dfdfs,sdf,dfs,df"
a = line.split(',')
print(a)
```

    ['ddf', 'dfdf', 'dfdfs', 'sdf', 'dfs', 'df']


## 字符串转数字


```python
a = '4'

print(int(a))

print(type(int(a)))
```

    4
    <class 'int'>

