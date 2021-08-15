# 安全攻击

## XSS攻击

### 反射型

定义：发出请求时，XSS代码出现在URL中，作为输入提交到服务器端，服务器端解析后响应，XSS代码随着响应内容一起传回浏览器，最后浏览器解析执行XSS代码。这个过程像一次反射，故叫反射型XSS

### 存储型

定义：存储型XSS和反射型XSS的差别仅仅在于，提交的代码会存储在服务器端（数据库、内存、文件系统等），下次请求目标页面时不用再提交XSS代码

## XSS 的防范措施

### 编码

对用户输入的数据进行HTML Entity编码

### 过滤

移除用户上传的DOM属性，如onerror等
移除用户上传的Style节点，Script节点，iframe节点等

### 校正

避免直接对HTML Entity编码
使用DOM Parse转换，校正不配对的DOM标签


## 脚本库

* [Pure-JavaScript-HTML5-Parser](https://github.com/blowsie/Pure-JavaScript-HTML5-Parser)
* [he](https://github.com/mathiasbynens/he)

## 参考

* [慕课网](https://www.imooc.com/learn/812)

