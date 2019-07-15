参考：[手写new](https://github.com/mqyqingfeng/Blog/issues/13)


在调用  `new`  的过程中会发生以上四件事情：

1.  新生成了一个对象
2.  链接到原型
3.  绑定 this
4.  返回新对象

根据以上几个过程，我们也可以试着来自己实现一个  `new`

```
function create() {
  let obj = {}
  let Con = [].shift.call(arguments)
  obj.__proto__ = Con.prototype
  let result = Con.apply(obj, arguments)
  return result instanceof Object ? result : obj
}

```

以下是对实现的分析：

-   创建一个空对象
-   获取构造函数
-   设置空对象的原型
-   绑定  `this`  并执行构造函数
-   确保返回值为对象

对于对象来说，其实都是通过  `new`  产生的，无论是  `function Foo()`  还是  `let a = { b : 1 }`  。

对于创建一个对象来说，更推荐使用字面量的方式创建对象（无论性能上还是可读性）。因为你使用  `new Object()`  的方式创建对象需要通过作用域链一层层找到  `Object`，但是你使用字面量的方式就没这个问题。

```
function Foo() {}
// function 就是个语法糖
// 内部等同于 new Function()
let a = { b: 1 }
// 这个字面量内部也是使用了 new Object()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MDIwOTIwMjZdfQ==
-->