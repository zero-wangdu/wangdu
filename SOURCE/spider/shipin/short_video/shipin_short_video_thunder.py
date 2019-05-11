import csv
import datetime

# import SOURCE.spider.ConfigHtml as Config
import os
import sys

import spider.common.ConfigHtml as Config
import time

# 下载 -- 短视频
from spider.common.MyLogRecord import SAVE_CSV_FILE


class shortVideoThunder(object):
    def __init__(self):
        self.url = 'https://{}{}'
        # self.baseUrl = 'www.ea235.com'
        self.baseUrl = 'www.776ut.com'

        ABS_PATH = os.path.dirname(sys.argv[0])

        self.fileName = '000_short_video_all.csv'
        self.file_path = ABS_PATH + '/' + self.fileName



    def run(self):
        with open('000_short_video_all.csv', 'r') as f:
            self.csv_file = csv.reader(f)
            for line in self.csv_file:
                print(line)

                name = line[0]
                page_url = line[1]

                url = self.url.format(self.baseUrl, page_url)

                try:
                    content = Config.get_content(url)
                    https = Config.xpath_content(content, '//input[@id="lin1k0"]/@value')
                    thunder = Config.xpath_content(content, '//input[@id="lin1k1"]/@value')
                except Exception as e:
                    print('error :' + str(e))


                https = https[0] if len(https) != 0 else ''
                thunder = thunder[0] if len(thunder) != 0 else ''

                print(name, page_url, https, thunder)
                SAVE_CSV_FILE('shipin_short_video_thunder.csv', [name, page_url, https, thunder], False)

                time.sleep(4)


shvideo = shortVideoThunder()
shvideo.run()