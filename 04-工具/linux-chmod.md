# linux 之chmod命令

## chmod 常用命令

### 第一种方式

> chmod [{ugoa}{+-=}{rwx}] [文件或目录]

- u:user(所有者): 即文件或目录的所有者。
- g:group(所属组): 即与文件属主有相同组ID的所有用户
- o:other: 其他用户
- a:所有用户
- +-:增加权限/删除权限
- r:读
- w:写
- x:执行

举例：

```bash
chmod u+wrx script.py // 给script.py 所有者增加读写执行的权限
chmod a+wrx script.py // 给script.py 所有用户增加读写执行的权限
```

### 第二种方式(常用)

> chmod -R [mode=421] [文件或目录]

- 4: 读
- 2: 写
- 1: 执行

第一位：user
第二位：group
第三位：other

-R: 代表递归修改

```bash
sudo chmod  777 /hurenxiang // 将hurenxiang这个文件夹权限改为对所有用户可读，可写，可执行

sudo chmod 775 /etc/caiyao // 将caiyao这个文件夹权限改为其他用户不可写
```

**注意：更改命令时，可能会引发git的文件变更，用一下命令在.git目录中输入，即可解决**

> git config core.filemode false


## 参考文献

* <https://blog.csdn.net/jerrytomcat/article/details/81744860>
* [菜鸟]('https://www.runoob.com/linux/linux-comm-chmod.html#:~:text=%E5%91%BD%E4%BB%A4%20chmod%20%E5%B0%86%E4%BF%AE%E6%94%B9%20who%20%E6%8C%87%E5%AE%9A%E7%9A%84%E7%94%A8%E6%88%B7%E7%B1%BB%E5%9E%8B%E5%AF%B9%E6%96%87%E4%BB%B6%E7%9A%84%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%EF%BC%8C%E7%94%A8%E6%88%B7%E7%B1%BB%E5%9E%8B%E7%94%B1%E4%B8%80%E4%B8%AA%E6%88%96%E8%80%85%E5%A4%9A%E4%B8%AA%E5%AD%97%E6%AF%8D%E5%9C%A8,who%20%E7%9A%84%E4%BD%8D%E7%BD%AE%E6%9D%A5%E8%AF%B4%E6%98%8E%EF%BC%8C%E5%A6%82%20who%20%E7%9A%84%E7%AC%A6%E5%8F%B7%E6%A8%A1%E5%BC%8F%E8%A1%A8%E6%89%80%E7%A4%BA%3A%20chmod%E5%91%BD%E4%BB%A4%E5%8F%AF%E4%BB%A5%E4%BD%BF%E7%94%A8%E5%85%AB%E8%BF%9B%E5%88%B6%E6%95%B0%E6%9D%A5%E6%8C%87%E5%AE%9A%E6%9D%83%E9%99%90%E3%80%82%20%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95%E7%9A%84%E6%9D%83%E9%99%90%E4%BD%8D%E6%98%AF%E7%94%B19%E4%B8%AA%E6%9D%83%E9%99%90%E4%BD%8D%E6%9D%A5%E6%8E%A7%E5%88%B6%EF%BC%8C%E6%AF%8F%E4%B8%89%E4%BD%8D%E4%B8%BA%E4%B8%80%E7%BB%84%EF%BC%8C%E5%AE%83%E4%BB%AC%E5%88%86%E5%88%AB%E6%98%AF%E6%96%87%E4%BB%B6%E6%89%80%E6%9C%89%E8%80%85%EF%BC%88User%EF%BC%89%E7%9A%84%E8%AF%BB%E3%80%81%E5%86%99%E3%80%81%E6%89%A7%E8%A1%8C%EF%BC%8C%E7%94%A8%E6%88%B7%E7%BB%84%EF%BC%88Group%EF%BC%89%E7%9A%84%E8%AF%BB%E3%80%81%E5%86%99%E3%80%81%E6%89%A7%E8%A1%8C%E4%BB%A5%E5%8F%8A%E5%85%B6%E5%AE%83%E7%94%A8%E6%88%B7%EF%BC%88Other%EF%BC%89%E7%9A%84%E8%AF%BB%E3%80%81%E5%86%99%E3%80%81%E6%89%A7%E8%A1%8C%E3%80%82')
