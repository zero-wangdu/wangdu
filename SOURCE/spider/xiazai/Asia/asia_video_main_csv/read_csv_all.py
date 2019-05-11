import csv
import os
import sys


def file_remote_all():
    ABS_PATH = os.path.dirname(sys.argv[0])

    file_li = os.listdir(ABS_PATH)

    print(file_li)

    fileName = '000_ziazai_asia_video_all.csv'
    file_path = ABS_PATH + '/' + fileName

    if os.path.exists(file_path):
        file_li.remove(fileName)

    with open(file_path, 'w', encoding='utf-8', newline='') as allf:
        writer = csv.writer(allf)
        for i in file_li:
            print(i)
            if i.find('.csv') == -1:
                continue

            f = open(ABS_PATH+'/'+i, 'r', encoding='utf-8')
            csv_file = csv.reader(f)
            for line in csv_file:
                name = line[0]
                name = get_right_name(name)
                url = line[1]
                writer.writerow([name, url])
                print(name, url)
            f.close()


def get_right_name(name):
    name = name.strip()
    name = name.replace('\n','')

    # name = name.replace('<','-')
    # name = name.replace('>','-')
    # name = name.replace('/','-')
    # name = name.replace('\\','-')
    # name = name.replace(':','-')
    # name = name.replace('*','-')
    # name = name.replace('"','-')
    # name = name.replace('?','-')
    # name = name.replace('→','-')

    return name


file_remote_all()


