'''
Author: Mr.Mei
Date: 2021-11-25 15:46:22
'''
from pywebio.input import *
from pywebio.output import *

# 输入框
input_res = input("please input your name:")
print('browser input is:', input_res)

# 密码框
pwd_res = input("please input your password:", type=PASSWORD)
print('password:', pwd_res)

sle = select("选择按钮", ['北京', '西安', '成都'])
ckb = checkbox("Multiple Choices!", options=["a", 'b', 'c', 'd'])
radio = radio("Select any one", options=['1', '2', '3'])
tar = textarea('Text Area', rows=3, placeholder='Multiple line text input')
sld = slider('这是滑动条', help_text='请滑动选择')  # 缺点是不能显示当前滑动的值
# 联动输入项
Country2City = {
    'China': ['西安', '北京', '成都'],
    'USA': ['纽约', '芝加哥', '佛罗里达'],
}
countries = list(Country2City.keys())

update_res = input_group(
    "国家和城市联动",
    [
        # 当国家发生变化的时候，onchange触发input_update方法去更新name=city的选项，更新内容为Country2City[c]，c代表国家的选项值
        select('国家', options=countries, name='country',
               onchange=lambda c: input_update('city', options=Country2City[c])),
        select('城市', options=Country2City[countries[0]], name='city')
    ]
)


print('what you said is:', tar)

# 文件上传
upload_res = file_upload(
    "please upload what you want to upload:", accept="image/*")

with open(upload_res.get('filename'), mode='wb') as f:  # 因为读取的图片内容是二进制，所以要以wb模式打开
    f.write(upload_res.get('content'))
print('what you uploaded is:', upload_res.get('filename'))


print(sld)

toast('提交成功')
put_markdown("""
    # 提示
    **提交成功**
    """, strip_indent=4)


print(update_res)
print(sle)
print(ckb)
print(radio)
print(tar)
