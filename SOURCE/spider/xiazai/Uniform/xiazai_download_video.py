import csv
import datetime

# import SOURCE.spider.ConfigHtml as Config
import os

import sys

import spider.common.ConfigHtml as Config
import time

# 下载 -- zhifu
from spider.common.MyLogRecord import MY_ERROR_LOG


class downloadVideo(object):
    def __init__(self):
        self.baseUrl = 'www.ea235.com'

    def run(self):
        for i in range(31,39+1):
            self.url = 'https://{}/xiazai/list-%E5%88%B6%E6%9C%8D%E4%B8%9D%E8%A2%9C-{}.html'.format(self.baseUrl, i)
            print(self.url)
            
            try:
                # 获取视频页的所有链接
                content = Config.get_content(self.url)
    
                self.a_href = Config.xpath_content(content, '//div[@id="tpl-img-content"]/li/a/@href')
                self.a_text = Config.xpath_content(content, '//div[@id="tpl-img-content"]/li/a/@title')
    
                print(self.a_href)
                print(self.a_text)
    
                # 保存视频页的所有链接
                fileName = datetime.datetime.now().strftime('%H%M%S%f')
                fileName = 'zifu_video_' + str(fileName) + '.csv'
    
                abs_path = os.path.dirname(sys.argv[0])
                filePath = abs_path + '/zifu_video_main_csv/'
    
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
    
                with open(filePath+fileName, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    for i in zip(self.a_text, self.a_href):
                        writer.writerow(i)
            except Exception as e:
                MY_ERROR_LOG(self.url)
                MY_ERROR_LOG(self.a_href)
                MY_ERROR_LOG(self.a_text)
                print('error : ', str(e))
            

            time.sleep(4)


video = downloadVideo()
video.run()