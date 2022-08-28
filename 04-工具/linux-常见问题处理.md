# linux 常见问题处理

## Linux 命令

### 查看端口

```
lsof -i:8888
```

### 杀死进程

```
kill pid
```

## node 相关

### 一、nvm 下载node

1.下载nvm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh
```

> 下载完成后需要让命令生效
> source .bashrc

2.列出远程可下载版本

```bash
nvm list-remote
```

3.安装相应的版本

```bash
nvm install v16.8.0
```

4.查看已安装的版本

```bash
nvm list
```

5.切换版本

```bash
nvm use v16.8.0
```

mac 安装 nvm 也很简单

```bash
brew install nvm # 再按照提示配置即可
```

这种方式，安装yarn

```bash
sudo npm install -g yarn
```

### 二、dnf安装Node

查看可安装node版本
> sudo dnf module list nodejs

node安装
> sudo dnf install nodejs

yarn安装

> curl -o- -L <https://yarnpkg.com/install.sh> | bash

```bash
# 写入.bashrc 文件
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
```

> source .bashrc

## ssh 常见问题

### 文件传输

命令格式：

scp username@servername:/path/filename /var/www/local_dir
将远程文件下载到本地 local_dir 目录，例如：

scp root@192.168.0.101:/var/www/test.txt /var/www/local_dir

> 把192.168.0.101上的 /var/www/test.txt 的文件下载到 /var/www/local_dir（本地目录）

2 上传文件

命令格式：

scp /path/filename username@servername:/path

例如：

```bash
scp /var/www/test.php  root@192.168.0.101:/var/www/
```

> 把本机 /var/www/test.php 文件上传到 192.168.0.101 服务器上的 /var/www/ 目录中。

3 下载目录

命令格式：

scp -r username@servername:/var/www/remote_dir/ /var/www/local_dir

> remote_dir 为远程目录，local_dir 为本地目录

例如：

```bash
scp -r root@192.168.0.101:/var/www/test /var/www/
```

4 上传目录
scp  -r local_dir username@servername:remote_dir

例如：

```bash
scp -r test  root@192.168.0.101:/var/www/
```

把当前目录下的 test 目录上传到服务器的 /var/www/ 目录

5 指定端口
指定端口用-P参数，注意是大写的P，例如：

```bash
scp -P 8000 -r test root@192.168.0.101:/var/www/
```

### ssh连接长时间不操作自动断开问题

1、修改服务器端参数

/etc/ssh/sshd_config 添加内容：

ClientAliveInterval  60 // 向客户端每60秒发一次保持连接的信号

ClientAliveCountMax  60 // 如果客户端60次未响应就断开连接,

2、修改本地参数

ServerAliveInterval  60
ServerAliveCountMax  60

### 关闭ssh链接

- 法1：Ctrl+D
- 法2：输入 logout
