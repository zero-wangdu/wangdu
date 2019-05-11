from lxml import etree

html = etree.HTML('text')


baseUrl = "https://www.301ii.com"
html.xpath("//div[@class='row']//ul/li//a//@href")
html.xpath("//tbody/tr/td/input/@value")

homeUrl = "https://www.301ii.com/index/home.html"


# 亚洲
asiaUrl = "https://www.301ii.com/xiazai/list-%E4%BA%9A%E6%B4%B2%E7%94%B5%E5%BD%B1-1.html"
html.xpath("//ul/div[@id='tpl-img-content']/li/a/@href")
html.xpath("//ul/div[@id='tpl-img-content']/li/a/@title")
html.xpath("//tbody/tr/td/input/@value")

# 短视频
shotUrl = "https://www.301ii.com/shipin/list-%E7%9F%AD%E8%A7%86%E9%A2%91-1.html"

