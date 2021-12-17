# Jinja2 快速生成报告


## 一、引入相关库文件


```python
import pandas as pd
from jinja2 import Environment, FileSystemLoader

```

## 二、 编写代码

### 1. 基础渲染


```python
data = {'strategy_name': '第一个策略',
        'start_time': '2020-01-01',
        'end_time': '2021-06-01',
        'money': 20000}

env = Environment(loader=FileSystemLoader('./'))

template = env.get_template('jinjia.email-template.html')

with open("out.html", 'w+', encoding='utf-8') as f:
    out = template.render(strategy_name=data['strategy_name'],
                          start_time=data['start_time'],
                          end_time=data['end_time'],
                          money=data['money'])
    f.write(out)
    f.close()

```

### 2. 表格渲染


```python
df = pd.read_csv('jinjia.601318-中国平安-历史日行情.csv')

data = df.to_dict('records')

results = {}
results.update({'strategy_name': '第一个策略',
                'start_time': '2020-01-01',
                'end_time': '2021-06-01',
                'money': 20000,
                'items': data})

env = Environment(loader=FileSystemLoader('./'))

template = env.get_template('jinjia.email-template.html')

with open("out.html", 'w+', encoding='utf-8') as f:
    out = template.render(strategy_name=results['strategy_name'],
                          start_time=results['start_time'],
                          end_time=results['end_time'],
                          money=results['money'],
                          items=results['items'])
    f.write(out)
    f.close()

```
