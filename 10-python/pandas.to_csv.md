# to_csv 常用问题解决


## 如何删除pandas中产生的Unnamed:0列

```
pd.read_csv(path, index_col=0)
或
pd.to_csv(path, index=False)
```

```

```

## 防止读取csv股票代码000没有的方法

```
pd.read_csv('/Downloads/2020-3-14-CB.csv',dtype = object)

pd.read_csv('/Downloads/2020-3-14-CB.csv',converters = {'正股代码':str})
df['正股代码'] = df['正股代码'].astype('str') #将原本的int数据类型转换为文本

df['正股代码']  = df['正股代码'].str.zfill(6) #用的时候必须加上.str前缀

```

## 指定为int 类型

```
data = pd.read_csv('../data/moive_metadata.csv', dtype={'duration': int})
```

## 追加行

```
df_data.to_csv('data.csv', mode='a', header=False, index=None) 
```

## 读取并转换类型

```
df = pd.read_csv("apple.csv", parse_dates =["date"], index_col ="date") 
```
