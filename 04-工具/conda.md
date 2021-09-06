# conda 常用操作

## 查看有哪些包

```bash
conda list
```

## 查看当前存在哪些虚拟环境

```bash
conda env list 
conda info -e
```

## 检查更新当前conda

```bash
conda update conda
```

## Python创建虚拟环境

```bash
conda create -n your_env_name python=x.x
```

## 激活或者切换虚拟环境

```bash
Linux:  source activate your_env_name
Windows: activate your_env_name
```

## 对虚拟环境中安装额外的包

```bash
conda install -n your_env_name [package]
```

## 关闭当前虚拟环境

```bash
deactivate env_name
```

## 删除虚拟环境

```bash
conda remove -n your_env_name --all
```

## 删除环境钟的某个包

```bash
conda remove --name $your_env_name  $package_name 
```

## 查看镜像

```bash
conda config --show-sources
```

## 添加镜像

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

```

或者

``` bash
vim ~/.condarc

channels:

  - https://mirrors.ustc.edu.cn/anaconda/pkgs/main/

  - https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/

  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

  - defaults

show_channel_urls: true
```

## 国内的几个镜像

``` bash
# 添加清华的源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/


# 中科大镜像源
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/

# 阿里镜像源
conda config --add channels https://mirrors.aliyun.com/pypi/simple/

# 豆瓣的python的源
conda config --add channels https://pypi.douban.com/simple/


# 显示检索路径，每次安装包时会将包源路径显示出来
conda config --set show_channel_urls yes

conda config --set always_yes True

# 显示所有镜像通道路径命令
conda config --show channels


```

## 恢复默认镜像

```bash
conda config --remove-key channels
```

## 清除索引缓存

```bash
conda clean -i
```
