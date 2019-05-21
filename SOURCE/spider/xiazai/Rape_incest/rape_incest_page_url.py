import csv
import datetime

# import SOURCE.spider.ConfigHtml as Config
import os

import spider.common.ConfigHtml as Config
import time


# 下载 -- 短视频

class xiazaiVideo(object):
    def __init__(self):
        # self.baseUrl = 'www.ea235.com'
        # self.baseUrl = 'www.776ut.com'
        # self.baseUrl = 'www.897ut.com'
        # self.baseUrl = 'www.ec352.com'
        # self.baseUrl = 'www.876yt.com'
        self.baseUrl = 'www.de325.com'


    def run(self):
        for i in range(1, 31 + 1):
            self.url = 'https://{}/xiazai/list-%e5%bc%ba%e5%a5%b8%e4%b9%b1%e4%bc%a6-{}.html'.format(self.baseUrl, i)

            print(self.url)

            # 获取短视频页的所有链接
            content = Config.get_content(self.url)

            a_href = Config.xpath_content(content, '//div[@id="tpl-img-content"]/li/a/@href')
            a_text = Config.xpath_content(content, '//div[@id="tpl-img-content"]/li/a/@title')

            print(a_href)
            print(a_text)

            # 保存短视频页的所有链接
            fileName = datetime.datetime.now().strftime('%H%M%S%f')
            fileName = 'rape_incest_video_' + str(fileName) + '.csv'
            filePath = './rape_incest_csv/'
            if not os.path.exists(filePath):
                os.makedirs(filePath)

            with open(filePath + fileName, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for i in zip(a_text, a_href):
                    writer.writerow(i)

            time.sleep(4)


video = xiazaiVideo()
video.run()
