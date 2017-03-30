# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
__author__ = 'nsk'
import time
import random

from parsel import Selector
from selenium import webdriver

def crawler_single(url, index, driver):
    driver.get(url)
    print driver.title
    for i in range(0, 25):
        js="var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(random.random()*2+1)
        print i
    html = driver.page_source

    file_name = 'article_done/article_' + str(index) + '.html'
    file_output = open(file_name, 'w')
    file_output.write(html)
    print '%d is over' % index
    # driver.quit()


def main():
    result_list = []
    driver = webdriver.Firefox()
    for i in range(0, 5):
        file_name = 'SERPs/Results_' + str(i) + '.txt'
        file_tmp = open(file_name, 'r')
        for line in file_tmp.readlines():
            result_list.append(line)
    for index, url in enumerate(result_list):
        crawler_single(url, index, driver)

if __name__ == '__main__':
    main()
