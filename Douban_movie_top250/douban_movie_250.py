import requests
from bs4 import BeautifulSoup
import pprint


## 获取html网页

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里知道百度贴吧的编码是utf-8，爬取其他页面时建议使用：
        # r.encoding = r.apparent_encoding
        r.encoding = 'utf-8'
        return r.text
    except:
        return "ERROR"


# 获取详细内容
def get_content(url):
    print("开始抓取本页内容！")
    contents = []
    html = get_html(url)

    # 解析html, soup
    soup = BeautifulSoup(html, "lxml")

    # get Tags
    tags = soup.find_all("div", class_="item")
    # pprint.pprint(tags)

    for tag in tags:
        content = {}
        try:
            content['rank'] = tag.find("em", class_="").text.strip()
            content['title'] = tag.find("span", class_="title").text.strip()
            content['director'] = tag.find("p", class_="").text.strip()
            content['star'] = tag.find('span', class_="rating_num").text.strip()
            content['quote'] = tag.find('span', class_="inq").text.strip()
            contents.append(content)
        except:
            "Something Wrong happened!"
    return contents


def out2txt(dict):
    with open('douban250.txt', 'a+', encoding='utf-8') as f:
        for content in dict:
            f.write("排名:{} \t 标题:{} \t 导演:{} \t 评价:{} \t 简介:{} \n"
                    .format(content['rank'], content['title'], content['director'], content['star'], content['quote']))
        f.close()


def main(base_url, deep):
    url_list = []
    for i in range(deep):
        url_list.append(base_url + str(i * 25) + "&filter=")

    for url in url_list:
        content = get_content(url)
        out2txt(content)
    print("抓取完成！")


base_url = "https://movie.douban.com/top250?start="
deep = 10

if __name__ == '__main__':
    main(base_url, deep)
