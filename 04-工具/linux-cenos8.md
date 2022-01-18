# conos8 服务器命令记录

## 安装 Node

查看可安装 node 版本

> sudo dnf module list nodejs

安装 node

> sudo dnf install nodejs

## 安装 yarn

> curl -o- -L <https://yarnpkg.com/install.sh> | bash

```bash
# 写入.bashrc 文件
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
```

> source .bashrc

## 安装 nginx

<https://blog.csdn.net/Cs_Mervyn/article/details/120075477>

<https://cloud.tencent.com/developer/article/1924770>

nginx 地址：/usr/local/nginx/

配置地址：vi /usr/local/nginx/conf/nginx.conf

```
<!-- 启动 -->
/usr/local/nginx/sbin/nginx
<!-- 停止 -->
/usr/local/nginx/sbin/nginx -s stop
<!-- 退出 -->
/usr/local/nginx/sbin/nginx -s quit
<!-- 重启 -->
/usr/local/nginx/sbin/nginx -s reload

<!-- 查询nginx进程 -->
ps aux|grep nginx


<!-- 防火墙允许nginx -->
*firewall*-*cmd* --*zone=public* --*add*-*port=80/tcp* --*permanent*


<!-- 开机自启动 -->
vi /etc/rc.local

#增加一行
/usr/local/nginx/sbin/nginx

chmod 755 /etc/rc.local
```
