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
    img_tags = soup.find_all("img", attrs={"data-src": True})

    imgurl_file_path = os.path.join(os.path.dirname(__file__), "data", "imgurl.txt")
    with open(imgurl_file_path, "w", encoding="utf-8") as file:
        print("获得图片url中...")

        for img_tag in img_tags:
            data_src_value = img_tag["data-src"]
            file.write(data_src_value + "\n")

        print("图片url获取完成!")
