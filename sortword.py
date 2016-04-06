import re
dic = {}
file = open("Desktop/a.rtf",'r').read().splitlines()
for line in file:
    # 替换文本里面的各种符号，比如“--、''”等
    line = re.sub(r'[^\u4e00-\u94a5\w\d\-]',' ',line)
    line = re.sub(r"[^a-zA-Z'-]|\\s+|\t|\r",' ',line)
    line = re.sub(r"-{2,}",' ',line)
    line = re.sub(r"'{2,}",' ',line)
    # 使用空格分割来统计各个单词出现的次数
    for b in line.split():
        dic.setdefault(b.lower(),0)
        dic[b.lower()] +=1
# 进行倒序排序
li = sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
for word in li:
    print word