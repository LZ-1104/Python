import requests
from bs4 import BeautifulSoup

def web_scraper(url, tag, attributes={}):
    """
    爬取指定URL的网页内容，提取指定标签的内容。
    
    参数:
    url (str): 目标网页的URL。
    tag (str): 需要提取的HTML标签。
    attributes (dict): 需要提取的标签属性（可选）。
    
    返回:
    list: 提取的内容列表。
    """
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析HTML内容
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 提取指定标签的内容
        elements = soup.find_all(tag, attrs=attributes)
        
        # 提取标签中的文本内容
        content_list = [element.get_text(strip=True) for element in elements]
        
        return content_list
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP错误: {http_err}")
    except Exception as err:
        print(f"其他错误: {err}")

# 示例用法
if __name__ == "__main__":
    url = input("请输入目标URL: ")
    tag = input("请输入需要提取的标签: ")
    attributes_str = input("请输入标签属性（格式为key1=value1,key2=value2，留空表示无属性）: ")

    # 解析标签属性
    attributes = {}
    if attributes_str:
        attributes = dict(attr.split('=') for attr in attributes_str.split(','))

    content = web_scraper(url, tag, attributes)
    
    print("提取的内容:")
    for item in content:
        print(item)