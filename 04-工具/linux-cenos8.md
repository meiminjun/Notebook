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

### 安装 https

1. 找到 nginx 下载包, 解压 tar -zxvf nginx-1.21.2.tar.gz

2. 配置 ssh

```bash
cd nginx-1.15.9.tar.gz

./configure --prefix=/usr/local/nginx --with-http_ssl_module

```

有可能说找不到 openssl,执行 which openssl，查找位置,
但是有可能版本不对，需要用低版本

3. 指定 openssl 位置

先找一下 openssl 位置
whereis openssl

> ./configure --prefix=/usr/local/nginx --with-http_ssl_module --with-openssl=/home/openssl-1.1.1l

cenos 8 不能 openssl 高版本，只能用 1.1.1 版本

地址：<https://www.openssl.org/source/old/1.1.1/>

1. 编译

> make
> ps:这里如果已经安装好 nginx , 第二次安装千万别 make install (会重新安装)

5. 将 objs/nginx 移动到 /usr/local/nginx/sbin/nginx

```
cd objs/nginx

cp nginx /usr/local/nginx/sbin/
```

6. 启动 nginx

/usr/local/nginx/sbin/nginx
