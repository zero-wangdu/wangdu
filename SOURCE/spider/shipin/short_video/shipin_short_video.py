import csv
import datetime

# import SOURCE.spider.ConfigHtml as Config
import spider.common.ConfigHtml as Config
import time

# 下载 -- 短视频

class shortVideo(object):
    def __init__(self):
        self.baseUrl = 'www.ea235.com'

    def run(self):
        for i in range(108,109):
            url = 'https://{}/shipin/list-%E7%9F%AD%E8%A7%86%E9%A2%91-{}.html'.format(self.baseUrl, i)
            print(url)

            # 获取短视频页的所有链接
            content = Config.get_content(url)

            a_href = Config.xpath_content(content, '//*[@id="grid"]/li/a/@href')
            a_text = Config.xpath_content(content, '//*[@id="grid"]/li/a/@title')

            print(a_href)
            print(a_text)

            # 保存短视频页的所有链接
            fileName = datetime.datetime.now().strftime('%H%M%S%f')
            fileName = 'short_video_' + str(fileName) + '.csv'
            with open(fileName, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for i in zip(a_text, a_href):
                    writer.writerow(i)

            time.sleep(3)


            # url = self.baseUrl + a_href
            # content = Config.get_content(url)
            # https = Config.xpath_content(content, '//input[@id="lin1k0"]/@value')
            # thunder = Config.xpath_content(content, '//input[@id="lin1k1"]/@value')
            #
            #
            # fileName = datetime.datetime.now().strftime('%H%M%S%f')
            # fileName = str(fileName) + '.csv'
            #
            # f = open(fileName, encoding='utf-8', newline='')
            # writer = csv.writer(f)
            # writer.writerow([])



#
# url = 'https://www.ea235.com/shipin/list-%E7%9F%AD%E8%A7%86%E9%A2%91-{}.html'.format(i)
#
# content = Config.get_content(url)
#
# a_href = Config.xpath_content(content, '//*[@id="grid"]/li/a/@href')
# a_text = Config.xpath_content(content, '//*[@id="grid"]/li/a/@title')
#
#
# print(a_href)
# print(a_text)
#
#
# for i in range(10):
#     # print(time.time())
#     # print(int(time.time()))
#     time_now = datetime.datetime.now().strftime('%H%M%S%f')
#     print(time_now)
#     time.sleep(0.1)

shvideo = shortVideo()
shvideo.run()