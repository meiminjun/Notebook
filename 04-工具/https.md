# https 相关知识

## 证书生成

### 一、下载mkcert

mkcert 是一个用 GO 写的零配置专门用来本地环境 https 证书生成的工具。

> brew install mkcert

### 二、本地安装CA

```bash
mkcert -install

mkcert localhost 或者 你的域名

```

> **这里要改下后缀名**

### 配置webpack

```bash
module.exports = {
  devServer: {
    https: true,
    key: fs.readFileSync('/path/to/server.key'),
    cert: fs.readFileSync('/path/to/server.crt')
  }
};
```


