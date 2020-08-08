promise
===



参考：https://juejin.im/post/5b31a4b7f265da595725f322


```
p.then(function(value) {
   // fulfillment成功
  }, function(reason) {
  // rejection失败
});

//不过通常会使用catch()来捕获失败，上段代码通常写为：
p.then(function(value) {
    // fulfillment成功
}).catch(function(reason) {
    //rejection失败
}) 
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgxNjY4Njk3MV19
-->