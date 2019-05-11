import requests
from lxml import etree
import csv
import time

class AsiaVideoSpider(object):
    def __init__(self):
        self.baseUrl = "http://www.916ii.com"
        self.asiaUrl = "http://www.916ii.com/shipin/list-%E4%BA%9A%E6%B4%B2%E6%97%A0%E7%A0%81-"
        self.value_li = []
        self.headers = {
            "User-Agent":"Moziall/5.0"
        }
        self.fileName = 'asia_without_code.csv'

    # 获取页面li标签下所有a链接和title
    def getPageLi(self, url):
        page = requests.get(url=url, headers=self.headers)
        page.encoding = 'utf-8'
        html = etree.HTML(page.content)
        self.a_li = html.xpath("//ul/div[@id='tpl-img-content']/li/a/@href")
        self.title_li = html.xpath("//ul/div[@id='tpl-img-content']/li/a/@title")

        print(self.a_li)
        print(self.title_li)

    # 获取链接页面里的下载url
    def getPageUrl(self, href):
        url = self.baseUrl + href
        page = requests.get(url=url, headers=self.headers)
        page.encoding = 'utf-8'
        html = etree.HTML(page.content)
        value_li = html.xpath("//tbody/tr/td/input/@value")
        print(value_li)
        return value_li

    def start(self):
        startPage = int(input("请输入开始页面 : "))
        endPage = int(input("请输入结束页面 : "))
        fileName = input("请输入保存文件的名字 : ")
        if fileName:
            self.fileName = fileName + '.csv'


        if startPage is None:
            startPage = 1
        if endPage is None:
            endPage = 10

        for index in range(startPage, endPage+1):
            url = self.asiaUrl + str(index) + '.html'
            print(url)
            self.getPageLi(url)
            for i in self.a_li:
                print(i)
                self.value_li.append(self.getPageUrl(i))
                time.sleep(0.3)
            print(self.value_li)

            # 保存
            with open(self.fileName, 'a+', newline='') as f:
                writer = csv.writer(f)
                for i in range(len(self.a_li)):
                    writer.writerow([self.title_li[i], self.a_li[i], self.value_li[i][0], self.value_li[i][1]])

            # 清除
            self.value_li = []
            self.a_li = []
            self.title_li = []





if __name__ == '__main__':
    asia = AsiaVideoSpider()
    asia.start()
