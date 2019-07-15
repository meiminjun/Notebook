`instanceof`  可以正确的判断对象的类型，因为内部机制是通过判断对象的原型链中是不是能找到类型的  `prototype`。

我们也可以试着实现一下  `instanceof`

```
function myInstanceof(left, right) {
  let prototype = right.prototype
  left = left.__proto__
  while (true) {
    if (left === null || left === undefined)
      return false
    if (prototype === left)
      return true
    left = left.__proto__
  }
}

```

以下是对实现的分析：

-   首先获取类型的原型
-   然后获得对象的原型
-   然后一直循环判断对象的原型是否等于类型的原型，直到对象原型为  `null`，因为原型链最终为  `null`


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzY0NTE1Mjg5XX0=
-->