# coding=utf-8
__author__ = 'nsk'
import requests
from parsel import Selector

def main():
    url = 'http://www.sciencedirect.com/science/article/pii/S0378437117302121'
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Sa'
                 'fari/537.36'
    }
    z = requests.get(url, headers=headers)
    print z.status_code
    sel = Selector(text=z.text)
    print sel.xpath('//*[@id="s000090"]')

if __name__ == '__main__':
    main()
