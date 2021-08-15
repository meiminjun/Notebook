
undefined 与 null 区别？

  

参考：

  

  

历史背景：

[http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html](http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html)

  

原来，这与JavaScript的历史有关。1995年[JavaScript诞生](http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html)时，最初像Java一样，只设置了null作为表示"无"的值。

根据C语言的传统，null被设计成可以自动转为0。

但是，JavaScript的设计者Brendan Eich(布兰登  艾克)，觉得这样做还不够，有两个原因。

首先，null像在Java里一样，被当成一个对象。但是，JavaScript的数据类型分成原始类型（primitive）和复杂类型（complex）两大类，Brendan Eich觉得表示"无"的值最好不是对象。

其次，JavaScript的最初版本没有包括错误处理机制，发生数据类型不匹配时，往往是自动转换类型或者默默地失败。Brendan Eich觉得，如果null自动转为0，很不容易发现错误。

因此，Brendan Eich又设计了一个undefined。

  

  

JavaScript的最初版本是这样区分的：**null**是一个表示**"**无**"**的对象，转为数值时为**0**；**undefined**是一个表示**"**无**"**的原始值，转为数值时为**NaN**。

  

我个人的认为：**null** 是复杂类型中的“无”，**undefined** 代表的是原始类型中的“无”

  

用法：

  

**null**表示**"**没有对象**"**，即该处不应该有值。典型用法是：

（1）  作为函数的参数，表示该函数的参数不是对象。

（2）  作为对象原型链的终点。

  

**undefined**表示**"**缺少值**"**，就是此处应该有一个值，但是还没有定义。典型用法是：

（1）变量被声明了，但没有赋值时，就等于undefined。

（2)  调用函数时，应该提供的参数没有提供，该参数等于undefined。

（3）对象没有赋值的属性，该属性的值为undefined。

（4）函数没有返回值时，默认返回undefined。

  

**undefined** 与 **null**

实际上undefined值是派生自null值的，因此ECMA-262规定对它们的相等性测试要返回true:

  

```

console.log(null == undefined); //true

```

  

因为使用的是标准相等符==,这个操作符出于目的会转换其操作数为相同类型后再做比较，如果我们使用严格相等符比较，我们会发现它们是不相等的，因为严格相等符不会进行类型转换，然而undefined与null属于不同的类型，所以不相等。

  

```

console.log(null === undefined); //false

```

  

尽管null和undefined有这样的关系，但上面我们已经提到过了，它们的用途完全不同，我们在平常使用时一定要学会区分。

  

  

注意项：

  

由于undefined 可以被重写(例子如下)，所以不能直接判断 data === undefined ,  而需要使用void运算符，因为ECMAScript 规定，在使用void对后面的表达式求值，无论结果是多少，都会返回原始值undefined

  

```

var a

console.log(a === void 0) // true

```

  

重写代码如下：

  

```

(function() { var undefined = 'not is undefined'; console.log(undefined); //"not is undefined" console.log(typeof undefined) // "string" })()

  

```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyNjQwMDExNF19
-->