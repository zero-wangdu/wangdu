import os
import sys
import csv
import datetime

from SOURCE.spider.common.MyLogRecord import MY_ERROR_LOG


class changeFileName(object):
    def __init__(self):
        self.class_name = 'change_video_name.py'
        self.ABS_PATH = os.path.dirname(sys.argv[0])
        self.file_name = 'shipin_short_video_thunder_true.csv'
        self.file_path = self.ABS_PATH + '/' + self.file_name
        self.video_li = self.get_file_list(self.ABS_PATH, [self.class_name, self.file_name])

    def start(self):
        video_dic = {}
        with open(self.file_path, 'r', encoding='utf-8') as f:
            thunder_csv = csv.reader(f)
            for line in thunder_csv:
                name = line[2]
                if name == '':
                    print(line)
                    MY_ERROR_LOG(str(line))
                    continue
                name = name.strip().split('/')[-1]
                video_dic[name] = line

        print(video_dic)
        for item in self.video_li:
            if item in video_dic.keys():
                new_name = video_dic.get(item)[0]
                new_name = self.get_right_name(new_name)

                new_video_li = self.get_file_list(self.ABS_PATH, [self.class_name, self.file_name])
                if new_name in new_video_li:
                    time_str = datetime.datetime.now().strftime('%H%M%S%f')
                    new_name = new_name + '_' + time_str

                os.rename(self.ABS_PATH +'/'+item, new_name)



    def get_file_list(self, path, li):
        video_li = os.listdir(self.ABS_PATH)
        for i in li:
            if i in video_li:
                video_li.remove(i)
        return video_li

    def get_right_name(self, name):
        name = name.strip()
        name = name.replace('\n', '')
        name = name.replace('<', '-')
        name = name.replace('>', '-')
        name = name.replace('/', '-')
        name = name.replace('\\', '-')
        name = name.replace(':', '-')
        name = name.replace('*', '-')
        name = name.replace('"', '-')
        name = name.replace('?', '-')
        name = name.replace('→', '-')
        return name


chage = changeFileName()
chage.start()
