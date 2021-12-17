# python 的时间操作

## 引入库


```python
from datetime import datetime, date, timedelta
import time
```

## 一、今天





```python
# 第一种方式（更准确）：
today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(today)
# 第二种方式
# print(date.today())
# date.today().strftime("%Y-%m-%d %H:%M:%S")

```

    2021-09-16 10:28:45


## 二、昨天

```python
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d") 
```



```python
def utc2local(utc_dtm):
    # UTC 时间转本地时间（ +8:00 ）
    local_tm = datetime.fromtimestamp(0)
    utc_tm = datetime.utcfromtimestamp(0)
    offset = local_tm - utc_tm
    return utc_dtm + offset


def local2utc(local_dtm):
    # 本地时间转 UTC 时间（ -8:00 ）
    return datetime.utcfromtimestamp(local_dtm.timestamp())

utc_tm = datetime.utcnow()
# utc_tm = datetime(2012, 10, 26, 10, 00, 00)

print("src utc time:\t", utc_tm.strftime("%Y-%m-%d %H:%M:%S"))

# UTC 转本地
local_tm = utc2local(utc_tm)
print("tran loc time:\t", local_tm.strftime("%Y-%m-%d %H:%M:%S"))

# 本地转 UTC
utc_tran = local2utc(local_tm)
print("tran utc time:\t", utc_tran.strftime("%Y-%m-%d %H:%M:%S"))

```

    src utc time:	 2021-09-16 02:46:42
    tran loc time:	 2021-09-16 10:46:42
    tran utc time:	 2021-09-16 02:46:42


## 三、时间格式转字符串


```python
date_p = datetime.now().date()

str_p = str(date_p)

print(date_p, type(date_p))  # 2019-01-30

print(str_p, type(str_p))  # 2019-01-30

```

    2021-10-02 <class 'datetime.date'>
    2021-10-02 <class 'str'>


## 四、字符串转时间格式


```python
str_p = '2019-01-30 15:29:08'

dateTime_p = datetime.strptime(str_p, '%Y-%m-%d %H:%M:%S')

print(dateTime_p, type(dateTime_p))  # 2019-01-30 15:29:08

```

    2019-01-30 15:29:08 <class 'datetime.datetime'>


## 常用时间集合

* %y 两位数的年份表示（00-99）
* %Y 四位数的年份表示（000-9999）
* %m 月份（01-12）
* %d 月内中的一天（0-31）
* %H 24小时制小时数（0-23）
* %I 12小时制小时数（01-12）
* %M 分钟数（00=59）
* %S 秒（00-59）
* %a 本地简化星期名称
* %A 本地完整星期名称
* %b 本地简化的月份名称
* %B 本地完整的月份名称
* %c 本地相应的日期表示和时间表示
* %j 年内的一天（001-366）
* %p 本地A.M.或P.M.的等价符
* %U 一年中的星期数（00-53）星期天为星期的开始
* %w 星期（0-6），星期天为星期的开始
* %W 一年中的星期数（00-53）星期一为星期的开始
* %x 本地相应的日期表示
* %X 本地相应的时间表示
* %Z 当前时区的名称
* %% %号本身


```python
dt = datetime.now()
print('时间：(%Y-%m-%d %H:%M:%S %f): ', dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print('时间：(%Y-%m-%d %H:%M:%S %p): ', dt.strftime('%y-%m-%d %I:%M:%S %p'))
print('星期缩写%%a: %s ' % dt.strftime('%a'))
print('星期全拼%%A: %s ' % dt.strftime('%A'))
print('月份缩写%%b: %s ' % dt.strftime('%b'))
print('月份全批%%B: %s ' % dt.strftime('%B'))
print('日期时间%%c: %s ' % dt.strftime('%c'))
print('今天是这周的第%s天 ' % dt.strftime('%w'))
print('今天是今年的第%s天 ' % dt.strftime('%j'))
print('今周是今年的第%s周 ' % dt.strftime('%U'))
print('今天是当月的第%s天 ' % dt.strftime('%d'))
```

    时间：(%Y-%m-%d %H:%M:%S %f):  2021-11-09 17:31:43 153857
    时间：(%Y-%m-%d %H:%M:%S %p):  21-11-09 05:31:43 PM
    星期缩写%a: Tue 
    星期全拼%A: Tuesday 
    月份缩写%b: Nov 
    月份全批%B: November 
    日期时间%c: Tue Nov  9 17:31:43 2021 
    今天是这周的第2天 
    今天是今年的第313天 
    今周是今年的第45周 
    今天是当月的第09天 


## dataframe 中的时间处理

**在读取pd.to_csv 时，每次都是str 类型，这时候就需要转换为时间格式**


### 方式一：parse_dates 指定列（最佳方式）

```bash
df = pd.read_csv(
      f'./stock_kline_data/{file_name}.csv', parse_dates=['交易日期'])
```

### 方式二：to_datetime 方法（推荐）：

```bash
df.index = pd.to_datetime(df.index)
```

### 方式三: 处理单独列方法转换：

```bash

def str_to_date(str_p):
  return datetime.strptime(str_p, '%Y-%m-%d')

df.index = df.index.map(str_to_date)
```


## 五、[日期神器-pendulum](https://mp.weixin.qq.com/s?src=11&timestamp=1633661554&ver=3361&signature=B5ZLgnPnxngUf1Iu8MJWiWuuqNB29mfpKWuvvK9W5LvuQyZ7r4ouQHG6AqqXkB8BoZwllAT1NwjMFZxSFdqT8iAzHJNDtNDyHNftU9w0AX-6*xi1Y65-on7AA*Q4MGoU&new=1)

参考： `https://mp.weixin.qq.com/s?src=11&timestamp=1633661554&ver=3361&signature=B5ZLgnPnxngUf1Iu8MJWiWuuqNB29mfpKWuvvK9W5LvuQyZ7r4ouQHG6AqqXkB8BoZwllAT1NwjMFZxSFdqT8iAzHJNDtNDyHNftU9w0AX-6*xi1Y65-on7AA*Q4MGoU&new=1`


```python
import pendulum
```

### 1. 昨天、今天、明天


```python

d1 = pendulum.yesterday()  # 昨天
# 2021-10-02T00:00:00+08:00

print('昨天: ',d1)

d2 = pendulum.today()  # 今天
# 2021-10-03T00:00:00+08:00

print('今天: ', d2)

d3 = pendulum.tomorrow()  # 明天
# 2021-10-04T00:00:00+08:00

print('明天: ', d3)

d4= d2.diff(d1).in_days()  # 相差多少天

print('相差多少天: ', d4)

d2.diff(d1).in_hours()  # 相差多少小时
# 47

print('现在: ', pendulum.now())  # 现在的时间

```

    昨天:  2021-10-07T00:00:00+08:00
    今天:  2021-10-08T00:00:00+08:00
    明天:  2021-10-09T00:00:00+08:00
    相差多少天:  1
    现在:  2021-10-08T10:57:38.376706+08:00


### 2. 时间转字符串

* to_date_string 转化日期
* to_datetime_string 转化日期和时间
* to_time_string 转化时间
* to_formatted_date_string 转化为英文书写形式
* format 安装指定格式转化
* strftime 同 datetime 的格式化方法


```python
dt = pendulum.now()
print('1: ',dt.to_date_string())
# '1975-12-25'

print('2: ',dt.to_formatted_date_string())
# 'Dec 25, 1975'

print('3: ', dt.to_time_string())
# '14:15:16'

print('4: ', dt.to_datetime_string())
# '1975-12-25 14:15:16'

print('5: ', dt.to_day_datetime_string())
# 'Thu, Dec 25, 1975 2:15 PM'

# You can also use the format() method
print('6: ', dt.format('dddd Do [of] MMMM YYYY HH:mm:ss A'))
# 'Friday 8	 of October 2021 11:05:51 AM'

# Of course, the strftime method is still available
print('7: ', dt.strftime('%A %-d%t of %B %Y %I:%M:%S %p'))
# 'Thursday 25th of December 1975 02:15:16 PM'

```

    1:  2021-10-08
    2:  Oct 08, 2021
    3:  11:06:17
    4:  2021-10-08 11:06:17
    5:  Fri, Oct 8, 2021 11:06 AM
    6:  Friday 8th of October 2021 11:06:17 AM
    7:  Friday 8	 of October 2021 11:06:17 AM


### 3. 字符串转化为时间类型

* 可以直接转化，也可以在转化时指定时区
* 支持多种时间格式，如果不是标准的时间格式，需要添加参数 strict=False，这样 Pendulum 就会尽最大可能去猜


```python
dt = pendulum.parse('1975-05-21T22:00:00')
print('1: ', dt)
# '1975-05-21T22:00:00+00:00

# You can pass a tz keyword to specify the timezone
dt2 = pendulum.parse('1975-05-21T22:00:00', tz='Europe/Paris')
print('2: ', dt2)
# '1975-05-21T22:00:00+01:00'

# Not ISO 8601 compliant but common
dt3 = pendulum.parse('1975-05-21 22:00:00')
print('3: ', dt3)

dt4 = pendulum.parse('31-01-01', strict=False)
print('4: ', dt4)

dt5 = pendulum.parse('31/01/01', strict=False)
print('5: ', dt5)


dt6 = pendulum.parse('31/1/1', strict=False)
print('6: ', dt6)

```

    1:  1975-05-21T22:00:00+00:00
    2:  1975-05-21T22:00:00+01:00
    3:  1975-05-21T22:00:00+00:00
    4:  2031-01-01T00:00:00+00:00
    5:  2031-01-01T00:00:00+00:00
    6:  2031-01-01T00:00:00+00:00

