# conos8 服务器命令记录

## 安装Node

查看可安装node版本
> sudo dnf module list nodejs

安装node
> sudo dnf install nodejs

## 安装yarn

> curl -o- -L <https://yarnpkg.com/install.sh> | bash

```bash
# 写入.bashrc 文件
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
```

> source .bashrc
