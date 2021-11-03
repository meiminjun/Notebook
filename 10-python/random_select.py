import random

student = ['郑萍军', '唐鑫', '黎少忠', '余光生', '莫少华']  # 定义列表这里存放你要点名同学的名字


def pairs(members):
    str = ''
    jishu = False
    length = len(members)

    if (length % 2) == 0:
        jishu = False
    else:
        jishu = True

    random.shuffle(members)

    d = list(range(0, len(members), 2))

    for i in d:
        # 如果是奇数，则最后一个与随机数配对
        if jishu == True and i == d[-1]:
            luck = random.choice(members[:i])
            last_arrs = members[i:i+2]
            last_arrs.append(luck)
            # print(f'{last_arrs[0]} 与 {last_arrs[1]}代码评审')
            str += f'{last_arrs[0]} 与 {last_arrs[1]}\n'
        else:
            # print(members[i:i+2])
            arr = members[i:i+2]
            # print(f'{arr[0]} 与 {arr[1]}代码评审')
            str += f'{arr[0]} 与 {arr[1]}\n'
    return str


def pairs2(members):
    str = ''
    length = len(members)
    random.shuffle(members)
    for key, item in enumerate(members):
        if key == length-1:
            str += f'{item}==>{members[0]}'
        else:
            str += f'{item}==>'
    return str
