'''
Author: Mr.Mei
Date: 2021-09-05 17:48:11
'''
import glob
import os

# 执行命令
os.system('jupyter nbconvert --to markdown */*.ipynb')

# 获取当前文件夹下的所有.md 文件
files = glob.glob(r'./*/*.md')

# print(files)
home = """# [我的知识笔记](https://meiminjun.github.io/Notebook/#/)

"""
str = "- [首页](/)\n"
list = [str]
# tup = ()
fie_name_list = []

for file in files:
    file_path = file[file.find('/')+1:]
    file_name = file[file.rfind('/')+1:file.rfind('.')]
    tup = (file_name, file_path)
    fie_name_list.append(tup)
    # print(file_path)
    # str += f"  - [{file_name}]({file_path})\n"


# print(fie_name_list)
# 按名称排序
fie_name_list.sort()
# print('排序之后')
# print(fie_name_list)

for i in fie_name_list:
    file_name = i[0]
    file_path = i[1]
    # print(file_name)
    str += f"  - [{file_name}]({file_path})\n"
    home += f"- [{file_name}]({file_path})\n"

    # str+= f

# str = f"""- [首页](/)
#   - [tmux命令运用](/04-工具/linux-tmux.md)
#   - [210821-关于思考的总结](/doc/210821-self-关于思考的总结.md)
#   - [210822-关于工作流整理](/doc/210822-self-我的工作流.md)
#   - [210905-股票-交易计划](/doc/210905-交易计划.md)
# """

with open('_sidebar.md', 'w') as f:
    f.write(str)

with open('README.md', 'w') as f:
    f.write(home)
