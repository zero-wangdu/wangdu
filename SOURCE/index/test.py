import io
import sys

import chardet

import SOURCE.getGlobalFun.ConfigHtml as Config
from lxml import etree

from urllib.parse import urlparse

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

f = open('content.html', 'r', encoding='utf-8')
content = f.read()
f.close()

title_li = Config.xpath_content(content, "//section[@id='section-menu']/div/div/div/a/text()")

a_text = Config.xpath_content(content, "//section[@id='section-menu']//li/a/text()")
a_href = Config.xpath_content(content, "//section[@id='section-menu']//li/a/@href")

print(title_li)
print(a_text)
print(a_href)

for i in a_text:
    print(str(i))

# with open('a_text.txt', 'w') as f:
#     for i in a_text:
#         f.write(bytes.decode(i.text))
#         f.write('\n')

one = 0
two = len(a_text) / len(title_li) -1

menu_dic = {}

for item in title_li:
    print(item)
    menu_dic[item] = a_text[one:two]
    one = two + 1
    two += two

print(menu_dic)







