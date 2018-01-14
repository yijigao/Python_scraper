import requests
from bs4 import BeautifulSoup


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
            content['director'] = tag.find("p", class_="").text.strip().split(" ")[0]
            content['starring'] = tag.find("p", class_="").text.strip().split(" ")[1]
            content['time'] = tag.find("p", class_="").text.strip().split(" ")[2]
            content['country'] = tag.find("p", class_="").text.strip().split(" ")[3]
            content['genre'] = tag.find("p", class_="").text.strip().split(" ")[4]
            content['star'] = tag.find('span', class_="rating_num").text.strip()
            content['quote'] = tag.find('span', class_="inq").text.strip()
            contents.append(content)
        except:
            "Something Wrong happened!"
    return contents


def out2txt(dict):
    with open('douban250.txt', 'a+', encoding='utf-8') as f:
        for content in dict:
            f.write(content['rank'] + " "
                    + content['title'] + " "
                    + content['director'] + " "
                    + content['starring'] + " "
                    + content['time'] + " "
                    + content['country'] + " "
                    + content['genre'] + " "
                    + content['star'] + " "
                    + content['quote'] + " "
                    + "\n")
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
