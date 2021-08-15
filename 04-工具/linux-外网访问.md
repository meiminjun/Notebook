查看防火墙是否开启
systemctl status firewalld

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o7qpwu6j30oq05zdhk.jpg)

若没有开启则开启
systemctl start firewalld  关闭则start改为stop

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8d8punj30ux0ajadf.jpg)

stop后会是这个样子：

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8ghwcrj30pw082goq.jpg)

查看所有开启的端口
firewall-cmd --list-ports

注：启动防火墙后，默认没有开启任何端口，需要手动开启端口

防火墙开启端口访问
firewall-cmd --zone=public --add-port=80/tcp --permanent
命令含义：  --zone #作用域   --add-port=80/tcp #添加端口，格式为：端口/通讯协议   --permanent #永久生效，没有此参数重启后失效

注：开启后需要重启防火墙才生效

【重启命令】： firewall-cmd --reload

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8kbksxj30i402zaa0.jpg)

再执行 firewall-cmd --list-ports查看一次，则发现已开启：

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8mgtw3j30e101vjr8.jpg)

然后我再开启3306端口：

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8sbkypj30n5041mx9.jpg)

再次连接发现可以连上了

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8taearj310s0h0abp.jpg)

然后我又加上了我的 superset端口8088，也可以访问啦！！！棒！：

![img](https://tva1.sinaimg.cn/large/007S8ZIlgy1gi8o8xetlgj31f30jf0t9.jpg)
