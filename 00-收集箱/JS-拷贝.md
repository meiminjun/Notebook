JS 中的深拷贝与浅拷贝

  

  

浅拷贝：拷贝已存在的非对象属性的值和对象属性的引用

  

  

```

var o = { a:1, b: { x:1 } }

  

var a = ["1", "2", { x: 1 }]

  

var aC = Array.prototype.slice.call(a)

  

a[2].x = 3

  

console.log(a)

console.debug(aC)

  

// 同时改变

  

```

  

  

数组的浅拷贝： Array.prototype.slice.call() 、Array.prototype.concat

  

  

深拷贝：

  

  

// 递归实现一个简单的深拷贝

**function deepCopy**(**obj**) **{**

**if**(**!obj || typeof obj !== 'object'**) **{**

**throw new Error**(**'**参数有误**'**)

**}**

**var o = Array.isArray**(**obj**) **?** [] **: {}**

**for** (**var key in obj**) **{**

**if** (**obj.hasOwnProperty**(**key**)) **{**

**if** (**obj**[**key**] **&& typeof obj**[**key**] **=== 'object'**) **{**

**o**[**key**] **= Array.isArray**(**obj**[**key**]) **?** [] **: {}**

**o**[**key**] **= deepCopy**(**obj**[**key**])

**} else {**

**o**[**key**] **= obj**[**key**]

**}**

**}**

**}**

**return o**

**}**

  

  

  

  

// 利用JSON序列化实现一个深拷贝

**function** **deepClone**(source){

**return** JSON.parse(JSON.stringify(source));

}

  

缺点：

  

1、无法拷贝方法


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDI1NzcwNzU3XX0=
-->