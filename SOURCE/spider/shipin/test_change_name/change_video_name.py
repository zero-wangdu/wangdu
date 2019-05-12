import os
import sys
import csv
import datetime

def get_file_list(li=[]):
    video_li = os.listdir('.')
    for i in li:
        if i in video_li:
            video_li.remove(i)
    return video_li

def get_right_name(name):
    name = name.strip()
    # name = name.replace('\n', '')
    name = name.replace('<', '-')
    name = name.replace('>', '-')
    name = name.replace('/', '-')
    name = name.replace('\\', '-')
    name = name.replace(':', '-')
    name = name.replace('*', '-')
    name = name.replace('"', '-')
    name = name.replace('?', '-')
    name = name.replace('→', '-')
    name = name.replace('|', '-')
    return name


class_name = 'change_video_name.py'
file_name = 'shipin_short_video_thunder_true.csv'
video_li = get_file_list([class_name, file_name])


def start():
    video_dic = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        thunder_csv = csv.reader(f)
        for line in thunder_csv:
            name = line[2]
            if name == '':
                print('########',line)
                continue
            name = name.strip().split('/')[-1]
            video_dic[name] = line

    for item in video_li:
        if item in video_dic.keys():
            new_name = video_dic.get(item)[0]
            new_name = get_right_name(new_name)
            video_type = item.strip().split('.')[-1]

            new_video_li = get_file_list([class_name, file_name])
            temp = new_name + '.' + video_type
            if temp in new_video_li:
                time_str = datetime.datetime.now().strftime('%H%M%S%f')
                new_name = new_name + '_' + time_str
            try:
                os.rename(item, new_name + '.' + video_type)
            except Exception as e:
                print('########', str(item))
                print(str(e))

start()