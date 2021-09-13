# linux 常见问题处理

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
