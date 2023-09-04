#!/home/sinclair/uservenv/bin/python


import os
import time
import selenium

# 初始化浏览器驱动
chrome_options = Options()
chrome_options.headless = True
chrome_service = ChromeService(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


def get_img_urls(url):
    """获取页面中具有data-src属性的img元素的data-src值"""
    driver.get(url)
    img_elements = driver.find_elements_by_css_selector("img[data-src]")
    img_urls = []

    for img_element in img_elements:
        # 模拟点击图片元素
        img_element.click()

        # 等待一段时间，确保页面加载完成
        time.sleep(2)  # 可根据需要调整等待时间

        # 执行JavaScript脚本（这里只是示例，可以根据需求修改）
        js_script = """
            // 在这里执行你的JavaScript代码
            // 例如：获取某个属性的值
            return document.querySelector('your_selector').getAttribute('your_attribute');
        """
        img_url = driver.execute_script(js_script)

        if img_url:
            img_urls.append(img_url)

    return img_urls


def save_img_urls_to_file(img_urls, file_path):
    """将获取到的img URL写入文件"""
    with open(file_path, "w", encoding="utf-8") as file:
        for img_url in img_urls:
            file.write(img_url + "\n")


if __name__ == "__main__":
    url = "https://prts.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88"
    img_urls = get_img_urls(url)

    imgurl_file_path = os.path.join(os.path.dirname(__file__), "data", "imgurl.txt")
    save_img_urls_to_file(img_urls, imgurl_file_path)

    # 最后关闭浏览器
    driver.quit()
