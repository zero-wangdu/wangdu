import csv

import SOURCE.getGlobalFun.ConfigHtml as Config

content = Config.get_content('https://www.ai398.com/index/home.html')
with open('content.html', 'w', encoding='utf-8') as f:
    f.write(str(content))
print(content)

title_li = Config.xpath_content(content, "//section[@id='section-menu']/div/div/div/a/text()")

a_text = Config.xpath_content(content, "//section[@id='section-menu']//ul/li/a/text()")
a_href = Config.xpath_content(content, "//section[@id='section-menu']//ul/li/a/@href")

print(title_li)
print(a_text)
print(a_href)

with open('a_link_li.csv', 'a+', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for i in range(len(a_text)):
        writer.writerow([a_text[i], a_href[i]])

one = 0
two = len(a_text) / len(title_li)

menu_dic = {}

for item in title_li:
    print(item)
    menu_dic[item] = a_text[one:two]
    one = two
    two += two

print(menu_dic)


