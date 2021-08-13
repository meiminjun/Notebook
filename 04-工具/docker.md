## docker 

我理解的docker:

镜像类似于一个系统环境（Mac os、windows）

容器类似于一个在环境中单个应用

## 镜像

查看镜像：docker images

构建镜像：docker build -t meiminjun/myserver:v1 .

强制删除镜像：docker rmi -f <镜像id>

删除所有镜像：docker rmi $(docker images -q)

删除所有无用镜像：docker rmi -f $(docker images | grep "none" | awk '{print $3}')

## 容器

启动容器：docker run -t -i meiminjun/myweb:v1 /bin/bash  

运行容器：docker run -itd --name node-test node

查看运行时容器：docker ps

查看所有容器：docker pa -a

停止容器：docker stop 

删除容器：docker rm -f <容器id>

> 删除容器时，必须是停止状态

删除所有容器：docker rm $(docker ps -a -q)

查看容器运行日志：docker logs -f <容器id>

## 其他

docker login

docker push meiminjun/myweb