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

"2323%".endswith('%')
```




    True



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

b = '123'

print(float(b))
```

    4
    <class 'int'>
    123.0


## 字符串替换


```python
str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"))
# 替换不超过3次
print(str.replace("is", "was", 3))
```

    thwas was string example....wow!!! thwas was really string
    thwas was string example....wow!!! thwas is really string


## 提取指定文字


```python
import re

# pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 匹配模式
pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
string = '4.12 ufb:/ 复制打开抖音，看看【田甜甜🌻的作品】每次回娘家我妈竟然这样对我，这我以后还能回去吗？# ... https://v.douyin.com/6FGuN4g/'
url = re.findall(pattern,string)
u= url[0]

print(u)

# par = re.compile(r'http[s]?://v.douyin.com/(\w+?)/')
par = r'http[s]?://v.douyin.com/(\w+?)/'
re.findall(par, u)
```

    https://v.douyin.com/6FGuN4g/





    ['6FGuN4g']



## 正则字符串提取

如果我们有一个字符串”a123b456b”,如果我们想匹配a和最后一个b之间的所有值而非a和第一个出现的b之间的值,可以用?来控制正则贪婪和非贪婪匹配的情况. 代码如下:


```python
import re

str = "a123b456b"

# +？ 非贪婪
print(re.findall(r"a(.+?)b", str))
#输出['123']#?控制只匹配0或1个,所以只会输出和最近的b之间的匹配情况

print(re.findall(r"a(.+)b", str))
#输出['123b456']

print(re.findall(r"a(.*)b", str))
#输出['123b456']
```

    ['123']
    ['123b456']
    ['123b456']


## 多行匹配提取

如果你要多行匹配，那么需要加上re.S和re.M标志. 加上re.S后, .将会匹配换行符，默认.不会匹配换行符. 代码如下:


```python
str = "a23b\na34b"

re.findall(r"a(\d+)b.+a(\d+)b", str)
#输出[]
#因为不能处理str中间有\n换行的情况

re.findall(r"a(\d+)b.+a(\d+)b", str, re.S)
#s输出[('23', '34')]
```




    [('23', '34')]



加上re.M后,^$标志将会匹配每一行，默认^和$只会匹配第一行. 代码如下:


```python
str = "a23b\na34b"

print(re.findall(r"^a(\d+)b", str))
#输出['23']

re.findall(r"^a(\d+)b", str, re.M)
#输出['23', '34']
```

    ['23']





    ['23', '34']


