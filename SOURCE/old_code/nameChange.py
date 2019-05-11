import os
import csv

def getNameDic():
    f = open('asia_url.csv', 'r', encoding='gb18030')
    file = csv.reader(f)
    video_dic = {}
    for i in file:
        ename = i[2].split('/')[-1]
        suffix = ename.split('.')[-1]
        cname = i[0] + '.' + suffix
        video_dic[ename] = cname

    print(video_dic)
    return video_dic

video_dic = getNameDic()

abs_path = os.getcwd()
file_li = os.listdir(abs_path)
for f in file_li:
    temp = video_dic.get(f)
    if temp:
        os.rename(f, temp)

