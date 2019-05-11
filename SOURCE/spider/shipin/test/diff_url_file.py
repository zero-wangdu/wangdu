import csv
import os
import sys

path = os.path.dirname(sys.argv[0])

print(path)

all_url_csv = '000_short_video_all.csv'
thunder_csv = 'shipin_short_video_thunder.csv'
and_or_csv = 'and_or.csv'

path_url_csv = path + '/' + all_url_csv
path_thunder_csv = path + '/' + thunder_csv
path_and_or_csv = path + '/' + and_or_csv

url_f = open(path_url_csv, 'r', encoding='utf-8')
thunder_f = open(path_thunder_csv, 'r', encoding='utf-8')

url_csv = csv.reader(url_f)
thunder_csv = csv.reader(thunder_f)

url_dic = {}
thunder_dic = {}
and_or_dic = {}

for line in url_csv:
    url_dic[line[1]] = line

for line in thunder_csv:
    thunder_dic[line[1]] = line

for th_key in thunder_dic.keys():
    if th_key in url_dic.keys():
        url_dic.pop(th_key)


with open(path_and_or_csv, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for i in url_dic.values():
        writer.writerow(i)




url_f.close()
thunder_f.close()

