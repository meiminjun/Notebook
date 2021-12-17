# to_csv 常用问题解决

## 如何删除pandas中产生的Unnamed:0列

``` bash
pd.read_csv(path, index_col=0)
或
pd.to_csv(path, index=False)

```
