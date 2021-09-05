# python 的时间操作

## 引入库


```python
from datetime import datetime, date, timedelta

```

## 今天





```python
# today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# date.today()
date.today().strftime("%Y-%m-%d")

```




    '2021-09-05'



## 二、昨天

```python
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d") 
```

