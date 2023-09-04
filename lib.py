"""
Author: nightmare-mio wanglongwei2009@qq.com
Date: 2023-08-28 22:27:36
LastEditTime: 2023-08-29 00:03:49
Description: 请不要恶意请求
"""
import os
import urllib.request
from bs4 import BeautifulSoup
import re
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import parsel


def getURL(url):
    """爬取html"""
    chrome_options = Options()
    chrome_options.headless = True

    chrome_service = ChromeService(executable_path="/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get(url)

    js_file_url = "https://static.prts.wiki/widgets/release/common.ffe0d211.js"
    driver.execute_script(
        f"var script = document.createElement('script');"
        f"script.src = '{js_file_url}';"
        f"document.head.appendChild(script);"
    )

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    driver.quit()
    return soup


def data_processing():
    """爬取数据并进行处理"""

    url = r"https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"
    soup = getURL(url)

    # pattern = re.compile('https://prts.wiki/images/*')
    img_tags = soup.find_all('img', attrs={'data-src': True})
    for img_tag in img_tags:

        items = img_tag['data-src']

        imgurl_file_path = os.path.join(os.path.dirname(__file__), "data", "imgurl.txt")
        print("获得名字中...")
        with open(imgurl_file_path, 'w', encoding='utf-8') as file:
            # 遍历匹配的元素并写入文件
            # for item in items:
            file.write(items + '\n')
                # print("已获取%d个图片url")


    # for item in html.find_all("div", class_="avatar lazyloaded"):
    #     i += 1
    #     item_str = str(item)
    #     cn_name = re.findall(re.compile(r'data-src="([^"]+)"'), item_str)[0]
    #     sheet.cell(i, 1).value = cn_name
    #     print(str(cn_name) + "获取完成")

