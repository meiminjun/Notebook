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

## nginx https 配置



```

#user  nobody;
worker_processes  1;

#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

#pid        logs/nginx.pid;


events {
    worker_connections  1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    #keepalive_timeout  0;
    keepalive_timeout  65;

    #gzip  on;

    server {
        listen       80;
        # server_name  localhost;
        server_name  quantool.site;
        #将请求转成https
        rewrite ^(.*)$ https://$host$1 permanent;
        #charset koi8-r;
        #access_log  logs/host.access.log  main;
        location / {
            root   /home/www;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    server {
        listen       8000;
        # server_name  localhost;
        server_name  quantool.site;
        # listen       somename:8080;
        # server_name  somename  alias  another.alias;
        location / {
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header Host $host;
            root   html;
            index  index.html index.htm;
        }
    }


    # HTTPS server
    #
    server {
        # listen       443 ssl http2;
        listen       443 ssl;
        server_name  quantool.site;

        ssl_certificate      /usr/local/nginx/mycert/quantool.site.pem;
        ssl_certificate_key  /usr/local/nginx/mycert/quantool.site.key;

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        # 这一句最关键，否则无法成功
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
        ssl_prefer_server_ciphers  on;

        location / {
            root   /home/www;
            index  index.html index.htm;
        }
    }

}


```
