import requests
from lxml import etree

def get_content(url):
    headers = {'User-Agent':'Moziall/5.0'}
    html = requests.get(url=url, headers=headers)
    html.encoding = 'utf-8'
    return html.content


def xpath_content(content, xpath_str):
    html = etree.HTML(content)
    return html.xpath(xpath_str)
