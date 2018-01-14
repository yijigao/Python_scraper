###############################
###   爬取百度贴吧的信息   ####
###############################

import requests
from bs4 import BeautifulSoup


# 抓取网页
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


def get_content(url):
    """
    分析贴吧的网页文件。整理信息，保存在列表变量中
    """

    # 初始化一个列表来保存所有帖子的信息
    comments = []
    # 首先，我们需要爬取信息的网页下载到本地
    html = get_html(url)
    # print(html)  # 测试

    # 解析html
    soup = BeautifulSoup(html, 'lxml')
    # print(soup) # 测试

    # 按照之前的分析，找到所有具有'j_thread_list clearfix'属性的标签。返回一个列表
    liTags = soup.find_all('li', class_=' j_thread_list clearfix')
    # print(liTags)  # 测试

    # 通过循环找到帖子里我们需要的信息
    for li in liTags:
        # 初始化一个字典储存文章信息
        comment = {}
        try:
            # 开始筛选信息
            comment['title'] = li.find('a', class_="j_th_tit ").text.strip()
            comment['link'] = "http://tieba.baidu.com" + \
                              li.find('a', class_="j_th_tit ")['href']
            comment['name'] = li.find('span', class_="tb_icon_author "
                                        ).text.strip()
            comment['time'] = li.find('span', class_="pull-right is_show_create_time").text.strip()
            comment['replyNum'] = li.find('span', class_="threadlist_rep_num center_text").text.strip()
            comments.append(comment)
        except:
            print("出了点小问题, 不要紧:)",)
    return comments


def Out2File(dict):
    """
    将爬取到的文件写入到本地
    保存到当前目录的TB.txt贴吧文件中
    """
    with open('TB.txt', 'a+', encoding='utf-8') as f:
        for comment in dict:
            f.write('标题:{} \t 链接:{} \t 发帖人:{} \t 发帖时间:{} \t 回复数量:{} \n'
                    .format(comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
        print("当前页面爬取完成！")
        f.close()


def main(base_url, deep):
    url_list = []
    # 将所有需要爬取的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + "&pn=" + str(50 * i) + "#")
    print('所有网页已经下载到本地！ 开始筛选信息>>>>>>>>>')

    # 循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        Out2File(content)
        # print(content)
    print('所有信息装填完毕！')


base_url = "http://tieba.baidu.com/f?kw=wp7&ie=utf-8"

if __name__ == '__main__':
    main(base_url, 10)
