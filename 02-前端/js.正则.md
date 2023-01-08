# 正则表达式学习

## 最小2、最大95字符的mac地址校验


```javascript
var a =
  "B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D2-DD";
attr = /(([A-Za-z0-9]{2}-[A-Za-z0-9]{2})+){1,15}(-[A-Za-z0-9]{2})$/;
console.log(attr.test(a));

```

    true



```javascript
var a = "B2-D2-D3-23-D2-D3-23-";
a+= a
a+= a
a += "B2-D2-D2-D3";
console.log(a)
console.log(a.length)
```

    B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D3-23-D2-D3-23-B2-D2-D2-D3
    95

