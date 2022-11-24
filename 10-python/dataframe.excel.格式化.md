# excel 格式化

参考：https://cloud.tencent.com/developer/article/1853145



```python
import pandas as pd
import numpy as np

data = {
  '基金名称': ['白酒基金','消费基金', '食品基金', '军工基金', '食品饮料'],
  '基金规模': ['2.3','982.232','232.232', '343.2', '232.22323'],
  '2018': ['-23.23', '-33.23', '0.45', '45.32', '34.34'],
  '2019': ['-23.23', '23.23', '0.74', '64.32', '68.34'],
  '2020': ['43.23', '62.23', '5.34', '-45.32', '34.34'],
  '上任日期': ['2017-08-22 00:00:00','2017-08-22 00:00:00','2017-08-22 00:00:00','2012-05-22 00:00:00','2019-09-22 00:00:00']
}

df = pd.DataFrame(data)
df
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
      <th>基金名称</th>
      <th>基金规模</th>
      <th>2018</th>
      <th>2019</th>
      <th>2020</th>
      <th>上任日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>白酒基金</td>
      <td>2.3</td>
      <td>-23.23</td>
      <td>-23.23</td>
      <td>43.23</td>
      <td>2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>消费基金</td>
      <td>982.232</td>
      <td>-33.23</td>
      <td>23.23</td>
      <td>62.23</td>
      <td>2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>食品基金</td>
      <td>232.232</td>
      <td>0.45</td>
      <td>0.74</td>
      <td>5.34</td>
      <td>2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>军工基金</td>
      <td>343.2</td>
      <td>45.32</td>
      <td>64.32</td>
      <td>-45.32</td>
      <td>2012-05-22 00:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>食品饮料</td>
      <td>232.22323</td>
      <td>34.34</td>
      <td>68.34</td>
      <td>34.34</td>
      <td>2019-09-22 00:00:00</td>
    </tr>
  </tbody>
</table>
</div>



## 排序

- ascending: False, 降序
- ascending: True, 升序


```python
# df_consume = df.reset_index(drop=True)
df_order = df.sort_values('基金规模', ascending=False).head(10)
df_order
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
      <th>基金名称</th>
      <th>基金规模</th>
      <th>2018</th>
      <th>2019</th>
      <th>2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>消费基金</td>
      <td>982.232</td>
      <td>-33.23</td>
      <td>23.23</td>
      <td>62.23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>军工基金</td>
      <td>343.2</td>
      <td>45.32</td>
      <td>64.32</td>
      <td>-45.32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>食品基金</td>
      <td>232.232</td>
      <td>0.45</td>
      <td>0.74</td>
      <td>5.34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>食品饮料</td>
      <td>232.22323</td>
      <td>34.34</td>
      <td>68.34</td>
      <td>34.34</td>
    </tr>
    <tr>
      <th>0</th>
      <td>白酒基金</td>
      <td>2.3</td>
      <td>-23.23</td>
      <td>-23.23</td>
      <td>43.23</td>
    </tr>
  </tbody>
</table>
</div>



## 隐藏列


```python
df2 = df.style.hide_index().hide_columns(['2020'])
df2
```




<style type="text/css">
</style>
<table id="T_68d92_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_68d92_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_68d92_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_68d92_row0_col2" class="data row0 col2" >-23.23</td>
      <td id="T_68d92_row0_col3" class="data row0 col3" >-23.23</td>
    </tr>
    <tr>
      <td id="T_68d92_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_68d92_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_68d92_row1_col2" class="data row1 col2" >-33.23</td>
      <td id="T_68d92_row1_col3" class="data row1 col3" >23.23</td>
    </tr>
    <tr>
      <td id="T_68d92_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_68d92_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_68d92_row2_col2" class="data row2 col2" >0.45</td>
      <td id="T_68d92_row2_col3" class="data row2 col3" >0.74</td>
    </tr>
    <tr>
      <td id="T_68d92_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_68d92_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_68d92_row3_col2" class="data row3 col2" >45.32</td>
      <td id="T_68d92_row3_col3" class="data row3 col3" >64.32</td>
    </tr>
    <tr>
      <td id="T_68d92_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_68d92_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_68d92_row4_col2" class="data row4 col2" >34.34</td>
      <td id="T_68d92_row4_col3" class="data row4 col3" >68.34</td>
    </tr>
  </tbody>
</table>




## 查看格式


```python
df.dtypes
```




    基金名称    object
    基金规模    object
    2018    object
    2019    object
    2020    object
    上任日期    object
    dtype: object



## 指定列格式化


```python
# df

df[['2018','2019', '2020']] = df[['2018', '2019', '2020']].applymap(float)
df[['2018', '2019', '2020']].dtypes
```




    2018    float64
    2019    float64
    2020    float64
    dtype: object



## 设置颜色

axis,0列(凌冽)
axis,1行

高亮指定列的最小值、最大值


```python

df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .highlight_max(axis=0,subset=['2018','2019','2020'])\
  .highlight_min(axis=0,subset=['2018','2019','2020'])
```




<style type="text/css">
#T_b02ad_row0_col3, #T_b02ad_row1_col2, #T_b02ad_row1_col4, #T_b02ad_row3_col2, #T_b02ad_row3_col4, #T_b02ad_row4_col3 {
  background-color: yellow;
}
</style>
<table id="T_b02ad_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_b02ad_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_b02ad_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_b02ad_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_b02ad_row0_col3" class="data row0 col3" >-23.23</td>
      <td id="T_b02ad_row0_col4" class="data row0 col4" >43.23</td>
    </tr>
    <tr>
      <td id="T_b02ad_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_b02ad_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_b02ad_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_b02ad_row1_col3" class="data row1 col3" >23.23</td>
      <td id="T_b02ad_row1_col4" class="data row1 col4" >62.23</td>
    </tr>
    <tr>
      <td id="T_b02ad_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_b02ad_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_b02ad_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_b02ad_row2_col3" class="data row2 col3" >0.74</td>
      <td id="T_b02ad_row2_col4" class="data row2 col4" >5.34</td>
    </tr>
    <tr>
      <td id="T_b02ad_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_b02ad_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_b02ad_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_b02ad_row3_col3" class="data row3 col3" >64.32</td>
      <td id="T_b02ad_row3_col4" class="data row3 col4" >-45.32</td>
    </tr>
    <tr>
      <td id="T_b02ad_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_b02ad_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_b02ad_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_b02ad_row4_col3" class="data row4 col3" >68.34</td>
      <td id="T_b02ad_row4_col4" class="data row4 col4" >34.34</td>
    </tr>
  </tbody>
</table>




### 指定高亮区间值


```python

df.style.hide_index()\
  .highlight_between(left=-0.2,right=30,subset=['2018','2019','2020'])
```




<style type="text/css">
#T_e0cc5_row1_col3, #T_e0cc5_row2_col2, #T_e0cc5_row2_col3, #T_e0cc5_row2_col4 {
  background-color: yellow;
}
</style>
<table id="T_e0cc5_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
      <th class="col_heading level0 col5" >上任日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_e0cc5_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_e0cc5_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_e0cc5_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_e0cc5_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_e0cc5_row0_col4" class="data row0 col4" >43.230000</td>
      <td id="T_e0cc5_row0_col5" class="data row0 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_e0cc5_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_e0cc5_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_e0cc5_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_e0cc5_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_e0cc5_row1_col4" class="data row1 col4" >62.230000</td>
      <td id="T_e0cc5_row1_col5" class="data row1 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_e0cc5_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_e0cc5_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_e0cc5_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_e0cc5_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_e0cc5_row2_col4" class="data row2 col4" >5.340000</td>
      <td id="T_e0cc5_row2_col5" class="data row2 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_e0cc5_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_e0cc5_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_e0cc5_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_e0cc5_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_e0cc5_row3_col4" class="data row3 col4" >-45.320000</td>
      <td id="T_e0cc5_row3_col5" class="data row3 col5" >2012-05-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_e0cc5_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_e0cc5_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_e0cc5_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_e0cc5_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_e0cc5_row4_col4" class="data row4 col4" >34.340000</td>
      <td id="T_e0cc5_row4_col5" class="data row4 col5" >2019-09-22 00:00:00</td>
    </tr>
  </tbody>
</table>




### 指定范围高亮

- 2018年的年度涨跌幅度 -24~+0 范围;
- 2019年的年度涨跌幅度 0~24 范围;
- 2020年的年度涨跌幅度 0~30 范围;


```python
df.style.hide_index()\
  .highlight_between(left=[-24,0,0],right=[0,24,30],subset=['2018','2019','2020'],axis=1)
```




<style type="text/css">
#T_7a3e9_row0_col2, #T_7a3e9_row1_col3, #T_7a3e9_row2_col3, #T_7a3e9_row2_col4 {
  background-color: yellow;
}
</style>
<table id="T_7a3e9_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
      <th class="col_heading level0 col5" >上任日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_7a3e9_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_7a3e9_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_7a3e9_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_7a3e9_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_7a3e9_row0_col4" class="data row0 col4" >43.230000</td>
      <td id="T_7a3e9_row0_col5" class="data row0 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_7a3e9_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_7a3e9_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_7a3e9_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_7a3e9_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_7a3e9_row1_col4" class="data row1 col4" >62.230000</td>
      <td id="T_7a3e9_row1_col5" class="data row1 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_7a3e9_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_7a3e9_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_7a3e9_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_7a3e9_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_7a3e9_row2_col4" class="data row2 col4" >5.340000</td>
      <td id="T_7a3e9_row2_col5" class="data row2 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_7a3e9_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_7a3e9_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_7a3e9_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_7a3e9_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_7a3e9_row3_col4" class="data row3 col4" >-45.320000</td>
      <td id="T_7a3e9_row3_col5" class="data row3 col5" >2012-05-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_7a3e9_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_7a3e9_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_7a3e9_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_7a3e9_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_7a3e9_row4_col4" class="data row4 col4" >34.340000</td>
      <td id="T_7a3e9_row4_col5" class="data row4 col5" >2019-09-22 00:00:00</td>
    </tr>
  </tbody>
</table>




### 设置自定义颜色


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .highlight_max(axis=0,subset=['2018','2019','2020'], props='color:black;background-color:#99ff66')\
  .highlight_min(axis=0,subset=['2018','2019','2020'], props='color:black;font-weight:bold;background-color:#ee7621')
```




<style type="text/css">
#T_b4f24_row0_col3, #T_b4f24_row1_col2, #T_b4f24_row3_col4 {
  color: black;
  font-weight: bold;
  background-color: #ee7621;
}
#T_b4f24_row1_col4, #T_b4f24_row3_col2, #T_b4f24_row4_col3 {
  color: black;
  background-color: #99ff66;
}
</style>
<table id="T_b4f24_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_b4f24_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_b4f24_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_b4f24_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_b4f24_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_b4f24_row0_col4" class="data row0 col4" >43.230000</td>
    </tr>
    <tr>
      <td id="T_b4f24_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_b4f24_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_b4f24_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_b4f24_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_b4f24_row1_col4" class="data row1 col4" >62.230000</td>
    </tr>
    <tr>
      <td id="T_b4f24_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_b4f24_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_b4f24_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_b4f24_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_b4f24_row2_col4" class="data row2 col4" >5.340000</td>
    </tr>
    <tr>
      <td id="T_b4f24_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_b4f24_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_b4f24_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_b4f24_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_b4f24_row3_col4" class="data row3 col4" >-45.320000</td>
    </tr>
    <tr>
      <td id="T_b4f24_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_b4f24_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_b4f24_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_b4f24_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_b4f24_row4_col4" class="data row4 col4" >34.340000</td>
    </tr>
  </tbody>
</table>




### 添加色阶


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .background_gradient(cmap='Blues', subset=['基金规模'])
```




<style type="text/css">
#T_7a6df_row0_col1 {
  background-color: #f7fbff;
  color: #000000;
}
#T_7a6df_row1_col1 {
  background-color: #08306b;
  color: #f1f1f1;
}
#T_7a6df_row2_col1, #T_7a6df_row4_col1 {
  background-color: #c9ddf0;
  color: #000000;
}
#T_7a6df_row3_col1 {
  background-color: #a6cee4;
  color: #000000;
}
</style>
<table id="T_7a6df_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_7a6df_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_7a6df_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_7a6df_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_7a6df_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_7a6df_row0_col4" class="data row0 col4" >43.230000</td>
    </tr>
    <tr>
      <td id="T_7a6df_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_7a6df_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_7a6df_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_7a6df_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_7a6df_row1_col4" class="data row1 col4" >62.230000</td>
    </tr>
    <tr>
      <td id="T_7a6df_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_7a6df_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_7a6df_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_7a6df_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_7a6df_row2_col4" class="data row2 col4" >5.340000</td>
    </tr>
    <tr>
      <td id="T_7a6df_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_7a6df_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_7a6df_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_7a6df_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_7a6df_row3_col4" class="data row3 col4" >-45.320000</td>
    </tr>
    <tr>
      <td id="T_7a6df_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_7a6df_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_7a6df_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_7a6df_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_7a6df_row4_col4" class="data row4 col4" >34.340000</td>
    </tr>
  </tbody>
</table>




可以通过对 low 和 high 值的设置，可以来调节背景颜色的范围，low 和 high 分别是压缩 低端和高端的颜色范围，其数值范围一般是 0~1 


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .background_gradient(cmap='Blues', subset=['基金规模'], low=0.3,high=0.9)
```




<style type="text/css">
#T_e3c74_row0_col1 {
  background-color: #dceaf6;
  color: #000000;
}
#T_e3c74_row1_col1 {
  background-color: #4d99ca;
  color: #f1f1f1;
}
#T_e3c74_row2_col1, #T_e3c74_row4_col1 {
  background-color: #c7dcef;
  color: #000000;
}
#T_e3c74_row3_col1 {
  background-color: #b8d5ea;
  color: #000000;
}
</style>
<table id="T_e3c74_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_e3c74_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_e3c74_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_e3c74_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_e3c74_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_e3c74_row0_col4" class="data row0 col4" >43.230000</td>
    </tr>
    <tr>
      <td id="T_e3c74_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_e3c74_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_e3c74_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_e3c74_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_e3c74_row1_col4" class="data row1 col4" >62.230000</td>
    </tr>
    <tr>
      <td id="T_e3c74_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_e3c74_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_e3c74_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_e3c74_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_e3c74_row2_col4" class="data row2 col4" >5.340000</td>
    </tr>
    <tr>
      <td id="T_e3c74_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_e3c74_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_e3c74_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_e3c74_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_e3c74_row3_col4" class="data row3 col4" >-45.320000</td>
    </tr>
    <tr>
      <td id="T_e3c74_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_e3c74_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_e3c74_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_e3c74_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_e3c74_row4_col4" class="data row4 col4" >34.340000</td>
    </tr>
  </tbody>
</table>




规模在20以下的，颜色最浅，规模70以上的，颜色最深，20~70亿之间的，颜色渐变


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .background_gradient(subset=['基金规模'], cmap='Blues',vmin=20,vmax=900)
```




<style type="text/css">
#T_4eb5a_row0_col1 {
  background-color: #f7fbff;
  color: #000000;
}
#T_4eb5a_row1_col1 {
  background-color: #08306b;
  color: #f1f1f1;
}
#T_4eb5a_row2_col1, #T_4eb5a_row4_col1 {
  background-color: #c8dcf0;
  color: #000000;
}
#T_4eb5a_row3_col1 {
  background-color: #a0cbe2;
  color: #000000;
}
</style>
<table id="T_4eb5a_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_4eb5a_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_4eb5a_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_4eb5a_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_4eb5a_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_4eb5a_row0_col4" class="data row0 col4" >43.230000</td>
    </tr>
    <tr>
      <td id="T_4eb5a_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_4eb5a_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_4eb5a_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_4eb5a_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_4eb5a_row1_col4" class="data row1 col4" >62.230000</td>
    </tr>
    <tr>
      <td id="T_4eb5a_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_4eb5a_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_4eb5a_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_4eb5a_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_4eb5a_row2_col4" class="data row2 col4" >5.340000</td>
    </tr>
    <tr>
      <td id="T_4eb5a_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_4eb5a_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_4eb5a_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_4eb5a_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_4eb5a_row3_col4" class="data row3 col4" >-45.320000</td>
    </tr>
    <tr>
      <td id="T_4eb5a_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_4eb5a_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_4eb5a_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_4eb5a_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_4eb5a_row4_col4" class="data row4 col4" >34.340000</td>
    </tr>
  </tbody>
</table>




### 数据条显示


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .bar(subset=['2018','2020'],color=['#99ff66','#ee7621'])
```




<style type="text/css">
#T_ffef4_row0_col2 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#99ff66 12.7%, transparent 12.7%);
}
#T_ffef4_row0_col4 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 82.3%, transparent 82.3%);
}
#T_ffef4_row1_col2, #T_ffef4_row3_col4 {
  width: 10em;
  height: 80%;
}
#T_ffef4_row1_col4, #T_ffef4_row3_col2 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 100.0%, transparent 100.0%);
}
#T_ffef4_row2_col2 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 42.9%, transparent 42.9%);
}
#T_ffef4_row2_col4 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 47.1%, transparent 47.1%);
}
#T_ffef4_row4_col2 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 86.0%, transparent 86.0%);
}
#T_ffef4_row4_col4 {
  width: 10em;
  height: 80%;
  background: linear-gradient(90deg,#ee7621 74.1%, transparent 74.1%);
}
</style>
<table id="T_ffef4_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_ffef4_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_ffef4_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_ffef4_row0_col2" class="data row0 col2" >-23.230000</td>
      <td id="T_ffef4_row0_col3" class="data row0 col3" >-23.230000</td>
      <td id="T_ffef4_row0_col4" class="data row0 col4" >43.230000</td>
    </tr>
    <tr>
      <td id="T_ffef4_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_ffef4_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_ffef4_row1_col2" class="data row1 col2" >-33.230000</td>
      <td id="T_ffef4_row1_col3" class="data row1 col3" >23.230000</td>
      <td id="T_ffef4_row1_col4" class="data row1 col4" >62.230000</td>
    </tr>
    <tr>
      <td id="T_ffef4_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_ffef4_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_ffef4_row2_col2" class="data row2 col2" >0.450000</td>
      <td id="T_ffef4_row2_col3" class="data row2 col3" >0.740000</td>
      <td id="T_ffef4_row2_col4" class="data row2 col4" >5.340000</td>
    </tr>
    <tr>
      <td id="T_ffef4_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_ffef4_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_ffef4_row3_col2" class="data row3 col2" >45.320000</td>
      <td id="T_ffef4_row3_col3" class="data row3 col3" >64.320000</td>
      <td id="T_ffef4_row3_col4" class="data row3 col4" >-45.320000</td>
    </tr>
    <tr>
      <td id="T_ffef4_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_ffef4_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_ffef4_row4_col2" class="data row4 col2" >34.340000</td>
      <td id="T_ffef4_row4_col3" class="data row4 col3" >68.340000</td>
      <td id="T_ffef4_row4_col4" class="data row4 col4" >34.340000</td>
    </tr>
  </tbody>
</table>




### 自定义设置颜色


```python

def max_value(x, color='red'):
    return np.where(x == np.nanmax(x.to_numpy()),
                    f"color: {color};background-color:yellow", None)
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .apply(max_value,axis=0,subset=['2018','2019','2020'])
```




<style type="text/css">
#T_83dd0_row1_col4, #T_83dd0_row3_col2, #T_83dd0_row4_col3 {
  color: red;
  background-color: yellow;
}
</style>
<table id="T_83dd0_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_83dd0_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_83dd0_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_83dd0_row0_col2" class="data row0 col2" >-23.23</td>
      <td id="T_83dd0_row0_col3" class="data row0 col3" >-23.23</td>
      <td id="T_83dd0_row0_col4" class="data row0 col4" >43.23</td>
    </tr>
    <tr>
      <td id="T_83dd0_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_83dd0_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_83dd0_row1_col2" class="data row1 col2" >-33.23</td>
      <td id="T_83dd0_row1_col3" class="data row1 col3" >23.23</td>
      <td id="T_83dd0_row1_col4" class="data row1 col4" >62.23</td>
    </tr>
    <tr>
      <td id="T_83dd0_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_83dd0_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_83dd0_row2_col2" class="data row2 col2" >0.45</td>
      <td id="T_83dd0_row2_col3" class="data row2 col3" >0.74</td>
      <td id="T_83dd0_row2_col4" class="data row2 col4" >5.34</td>
    </tr>
    <tr>
      <td id="T_83dd0_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_83dd0_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_83dd0_row3_col2" class="data row3 col2" >45.32</td>
      <td id="T_83dd0_row3_col3" class="data row3 col3" >64.32</td>
      <td id="T_83dd0_row3_col4" class="data row3 col4" >-45.32</td>
    </tr>
    <tr>
      <td id="T_83dd0_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_83dd0_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_83dd0_row4_col2" class="data row4 col2" >34.34</td>
      <td id="T_83dd0_row4_col3" class="data row4 col3" >68.34</td>
      <td id="T_83dd0_row4_col4" class="data row4 col4" >34.34</td>
    </tr>
  </tbody>
</table>




### 行列同时自定义


```python
def color_returns(val):
    if float(val) > 0:
        color = '#EE7621'  # light red
    elif float(val) < 0:
        color = '#99ff66'  # light green  '#99ff66'
    else:
        color = '#FFFAFA'  # ligth gray
    return f'background-color: {color}'

df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .applymap(color_returns,subset=pd.IndexSlice[1:5,['2018','2019','2020']])
```




<style type="text/css">
#T_854d7_row1_col2, #T_854d7_row3_col4 {
  background-color: #99ff66;
}
#T_854d7_row1_col3, #T_854d7_row1_col4, #T_854d7_row2_col2, #T_854d7_row2_col3, #T_854d7_row2_col4, #T_854d7_row3_col2, #T_854d7_row3_col3, #T_854d7_row4_col2, #T_854d7_row4_col3, #T_854d7_row4_col4 {
  background-color: #EE7621;
}
</style>
<table id="T_854d7_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_854d7_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_854d7_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_854d7_row0_col2" class="data row0 col2" >-23.23</td>
      <td id="T_854d7_row0_col3" class="data row0 col3" >-23.23</td>
      <td id="T_854d7_row0_col4" class="data row0 col4" >43.23</td>
    </tr>
    <tr>
      <td id="T_854d7_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_854d7_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_854d7_row1_col2" class="data row1 col2" >-33.23</td>
      <td id="T_854d7_row1_col3" class="data row1 col3" >23.23</td>
      <td id="T_854d7_row1_col4" class="data row1 col4" >62.23</td>
    </tr>
    <tr>
      <td id="T_854d7_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_854d7_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_854d7_row2_col2" class="data row2 col2" >0.45</td>
      <td id="T_854d7_row2_col3" class="data row2 col3" >0.74</td>
      <td id="T_854d7_row2_col4" class="data row2 col4" >5.34</td>
    </tr>
    <tr>
      <td id="T_854d7_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_854d7_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_854d7_row3_col2" class="data row3 col2" >45.32</td>
      <td id="T_854d7_row3_col3" class="data row3 col3" >64.32</td>
      <td id="T_854d7_row3_col4" class="data row3 col4" >-45.32</td>
    </tr>
    <tr>
      <td id="T_854d7_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_854d7_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_854d7_row4_col2" class="data row4 col2" >34.34</td>
      <td id="T_854d7_row4_col3" class="data row4 col3" >68.34</td>
      <td id="T_854d7_row4_col4" class="data row4 col4" >34.34</td>
    </tr>
  </tbody>
</table>




### 按范围锁定进行样式格式化


```python
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .applymap(color_returns, subset=pd.IndexSlice[3:2])
```




<style type="text/css">
</style>
<table id="T_1b26e_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_1b26e_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_1b26e_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_1b26e_row0_col2" class="data row0 col2" >-23.23</td>
      <td id="T_1b26e_row0_col3" class="data row0 col3" >-23.23</td>
      <td id="T_1b26e_row0_col4" class="data row0 col4" >43.23</td>
    </tr>
    <tr>
      <td id="T_1b26e_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_1b26e_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_1b26e_row1_col2" class="data row1 col2" >-33.23</td>
      <td id="T_1b26e_row1_col3" class="data row1 col3" >23.23</td>
      <td id="T_1b26e_row1_col4" class="data row1 col4" >62.23</td>
    </tr>
    <tr>
      <td id="T_1b26e_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_1b26e_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_1b26e_row2_col2" class="data row2 col2" >0.45</td>
      <td id="T_1b26e_row2_col3" class="data row2 col3" >0.74</td>
      <td id="T_1b26e_row2_col4" class="data row2 col4" >5.34</td>
    </tr>
    <tr>
      <td id="T_1b26e_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_1b26e_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_1b26e_row3_col2" class="data row3 col2" >45.32</td>
      <td id="T_1b26e_row3_col3" class="data row3 col3" >64.32</td>
      <td id="T_1b26e_row3_col4" class="data row3 col4" >-45.32</td>
    </tr>
    <tr>
      <td id="T_1b26e_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_1b26e_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_1b26e_row4_col2" class="data row4 col2" >34.34</td>
      <td id="T_1b26e_row4_col3" class="data row4 col3" >68.34</td>
      <td id="T_1b26e_row4_col4" class="data row4 col4" >34.34</td>
    </tr>
  </tbody>
</table>




### 共享样式

保存样式


```python
style1 = df.style.hide_index()\
                .highlight_min(axis=1,subset=['2018','2019','2020'],props='color:black;background-color:#99ff66')\
                .highlight_max(axis=1,subset=['2018','2019','2020'],props='color:black;background-color:#ee7621')\
                .highlight_null(props='color:white;background-color:darkblue')
style1
```




<style type="text/css">
#T_464b6_row0_col2, #T_464b6_row0_col3, #T_464b6_row1_col2, #T_464b6_row2_col2, #T_464b6_row3_col4, #T_464b6_row4_col2, #T_464b6_row4_col4 {
  color: black;
  background-color: #99ff66;
}
#T_464b6_row0_col4, #T_464b6_row1_col4, #T_464b6_row2_col4, #T_464b6_row3_col3, #T_464b6_row4_col3 {
  color: black;
  background-color: #ee7621;
}
</style>
<table id="T_464b6_">
  <thead>
    <tr>
      <th class="col_heading level0 col0" >基金名称</th>
      <th class="col_heading level0 col1" >基金规模</th>
      <th class="col_heading level0 col2" >2018</th>
      <th class="col_heading level0 col3" >2019</th>
      <th class="col_heading level0 col4" >2020</th>
      <th class="col_heading level0 col5" >上任日期</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td id="T_464b6_row0_col0" class="data row0 col0" >白酒基金</td>
      <td id="T_464b6_row0_col1" class="data row0 col1" >2.3</td>
      <td id="T_464b6_row0_col2" class="data row0 col2" >-23.23</td>
      <td id="T_464b6_row0_col3" class="data row0 col3" >-23.23</td>
      <td id="T_464b6_row0_col4" class="data row0 col4" >43.23</td>
      <td id="T_464b6_row0_col5" class="data row0 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_464b6_row1_col0" class="data row1 col0" >消费基金</td>
      <td id="T_464b6_row1_col1" class="data row1 col1" >982.232</td>
      <td id="T_464b6_row1_col2" class="data row1 col2" >-33.23</td>
      <td id="T_464b6_row1_col3" class="data row1 col3" >23.23</td>
      <td id="T_464b6_row1_col4" class="data row1 col4" >62.23</td>
      <td id="T_464b6_row1_col5" class="data row1 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_464b6_row2_col0" class="data row2 col0" >食品基金</td>
      <td id="T_464b6_row2_col1" class="data row2 col1" >232.232</td>
      <td id="T_464b6_row2_col2" class="data row2 col2" >0.45</td>
      <td id="T_464b6_row2_col3" class="data row2 col3" >0.74</td>
      <td id="T_464b6_row2_col4" class="data row2 col4" >5.34</td>
      <td id="T_464b6_row2_col5" class="data row2 col5" >2017-08-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_464b6_row3_col0" class="data row3 col0" >军工基金</td>
      <td id="T_464b6_row3_col1" class="data row3 col1" >343.2</td>
      <td id="T_464b6_row3_col2" class="data row3 col2" >45.32</td>
      <td id="T_464b6_row3_col3" class="data row3 col3" >64.32</td>
      <td id="T_464b6_row3_col4" class="data row3 col4" >-45.32</td>
      <td id="T_464b6_row3_col5" class="data row3 col5" >2012-05-22 00:00:00</td>
    </tr>
    <tr>
      <td id="T_464b6_row4_col0" class="data row4 col0" >食品饮料</td>
      <td id="T_464b6_row4_col1" class="data row4 col1" >232.22323</td>
      <td id="T_464b6_row4_col2" class="data row4 col2" >34.34</td>
      <td id="T_464b6_row4_col3" class="data row4 col3" >68.34</td>
      <td id="T_464b6_row4_col4" class="data row4 col4" >34.34</td>
      <td id="T_464b6_row4_col5" class="data row4 col5" >2019-09-22 00:00:00</td>
    </tr>
  </tbody>
</table>




使用样式


```python
df_fund_1 = df[['2018','2019','2020']]

df_fund_1.style.use(style1.export())
```




<style type="text/css">
#T_f491f_row0_col0, #T_f491f_row0_col1, #T_f491f_row1_col0, #T_f491f_row2_col0, #T_f491f_row3_col2, #T_f491f_row4_col0, #T_f491f_row4_col2 {
  color: black;
  background-color: #99ff66;
}
#T_f491f_row0_col2, #T_f491f_row1_col2, #T_f491f_row2_col2, #T_f491f_row3_col1, #T_f491f_row4_col1 {
  color: black;
  background-color: #ee7621;
}
</style>
<table id="T_f491f_">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th class="col_heading level0 col0" >2018</th>
      <th class="col_heading level0 col1" >2019</th>
      <th class="col_heading level0 col2" >2020</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_f491f_level0_row0" class="row_heading level0 row0" >0</th>
      <td id="T_f491f_row0_col0" class="data row0 col0" >-23.23</td>
      <td id="T_f491f_row0_col1" class="data row0 col1" >-23.23</td>
      <td id="T_f491f_row0_col2" class="data row0 col2" >43.23</td>
    </tr>
    <tr>
      <th id="T_f491f_level0_row1" class="row_heading level0 row1" >1</th>
      <td id="T_f491f_row1_col0" class="data row1 col0" >-33.23</td>
      <td id="T_f491f_row1_col1" class="data row1 col1" >23.23</td>
      <td id="T_f491f_row1_col2" class="data row1 col2" >62.23</td>
    </tr>
    <tr>
      <th id="T_f491f_level0_row2" class="row_heading level0 row2" >2</th>
      <td id="T_f491f_row2_col0" class="data row2 col0" >0.45</td>
      <td id="T_f491f_row2_col1" class="data row2 col1" >0.74</td>
      <td id="T_f491f_row2_col2" class="data row2 col2" >5.34</td>
    </tr>
    <tr>
      <th id="T_f491f_level0_row3" class="row_heading level0 row3" >3</th>
      <td id="T_f491f_row3_col0" class="data row3 col0" >45.32</td>
      <td id="T_f491f_row3_col1" class="data row3 col1" >64.32</td>
      <td id="T_f491f_row3_col2" class="data row3 col2" >-45.32</td>
    </tr>
    <tr>
      <th id="T_f491f_level0_row4" class="row_heading level0 row4" >4</th>
      <td id="T_f491f_row4_col0" class="data row4 col0" >34.34</td>
      <td id="T_f491f_row4_col1" class="data row4 col1" >68.34</td>
      <td id="T_f491f_row4_col2" class="data row4 col2" >34.34</td>
    </tr>
  </tbody>
</table>




## 导出excel


```python
def max_value(x, color='red'):
    return np.where(x == np.nanmax(x.to_numpy()),
                    f"color: {color};background-color:yellow", None)
df.style.hide_index()\
  .hide_columns(['上任日期'])\
  .apply(max_value,axis=0,subset=['2018','2019','2020'])\
  .to_excel('style_export.xlsx',engine = 'openpyxl')

```
