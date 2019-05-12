import requests
from lxml import etree


def get_content(url):
    try:
        headers = {'User-Agent':'Moziall/5.0'}
        html = requests.get(url=url, headers=headers)
        html.encoding = 'utf-8'
        return html.content
    except Exception as e:
        f = open('log.txt', 'a+', encoding='utf-8')
        f.write(url)
        f.write('\n')
        f.write(str(e))
        f.write('\n')
        f.write('\n')
        f.close()
        print(url, e)



def xpath_content(content, xpath_str):
    html = etree.HTML(content)
    return html.xpath(xpath_str)



def get_right_name(name):
    name = name.strip()
    name = name.replace('\n','')
    name = name.replace('<','-')
    name = name.replace('>','-')
    name = name.replace('/','-')
    name = name.replace('\\','-')
    name = name.replace(':','-')
    name = name.replace('*','-')
    name = name.replace('"','-')
    name = name.replace('?','-')
    name = name.replace('→','-')
    name = name.replace('|','-')

    return name
