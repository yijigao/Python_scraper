# 获取网易云音乐华语男歌手top100的热门50首歌曲及评论信息

爬虫库: requests
html解析: BeautifulSoup, lxml, xpath


## 1. 获取数据
### 1.1 获取歌手的artist id
网址http://music.163.com/#/discover/artist/cat?id=1001
爬取时使用上面的url发现没有内容，这个不是真实url,查看network

<img src="https://github.com/yijigao/Python_scraper/tree/master/cloud_music/libs/1.jpg" height="300", width="400">
真实的url是没有中间哪个“#”, 这点网页有点"鸡贼" = =

ok，开始获取想要的信息了
先把请求搞定，直接抄就是
```
def get_html(url):
    headers = {
        "Accept": "text/html, application / xhtml + xml, application / xml;\
                  q = 0.9, image / webp, image / apng, * / *;q = 0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh,zh-CN;q=0.9,ja;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "_iuqxldmzr_=32;"
                  " _ntes_nnid=773f2853ee69df661e6a4972f27f4726,1517319989559;"
                  " _ntes_nuid=773f2853ee69df661e6a4972f27f4726;"
                  " __utmz=94650624.1517319990.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;"
                  " __utmc=94650624; "
                  "JSESSIONID-WYYY=3Vwm8JIRVqlPdhzItnI6H4xeKG93m1N7Z0g1PZDBJ86orZsYA35yYJTDTC6swEk%5CXmzE1JFRt4N%2FThvUAAIWNgqBnbRjp%2FvzEvagFYvXcqIeq6%5CumvvarXQIzFtWWh%2BoOBzssbv0izoXyH0XpAuJYEDPYY0uFgd3o4SPaGFQ78SD8yye%3A1518870790654;"
                  " __utma=94650624.349500884.1517319990.1518862029.1518869311.3;"
                  " __utmb=94650624.2.10.1518869311 ",
        "DNT": "1",
        "Host": "music.163.com",
        "Referer": "http://music.163.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/64.0.3282.167 Safari/537.36"
    }
    r = requests.request("GET", url=url, headers=headers)
    return r.text
```

我准备先拿到华语男歌手top100的歌手网页id
大致是这个样子```<a href=" /artist?id=6452" class="nm nm-icn f-thide s-fc0" title="周杰伦的音乐">周杰伦</a>```

```
    url = "http://music.163.com/discover/artist/cat?id=1001"
    html = get_html(url)
    
    soup = BeautifulSoup(html, "lxml")
    sel = soup.find(class_="m-sgerlist")
    s_dict = {}
    for ele in sel.find_all('a'):
        if ele.text:
            s_dict[ele.text] = ele.get('href')
```
来看看结果, 目标基本达成~

```
>>> print(s_dict)
{'周杰伦': ' /artist?id=6452', '陈奕迅': ' /artist?id=2116', '薛之谦': ' /artist?id=5781', '林俊杰': ' /artist?id=3684', '李荣浩': ' /artist?id=4292', '张学友': ' /artist?id=6460'....
```

### 1.2 进入歌手页，获取热门50首歌曲
网址形式为```http://music.163.com/#/artist?id=6452```
F12 看看top50热门歌曲信息在哪，包裹在```<tbody></tbody>```中，然而使用soup打出来看却什么也没有
打开源码，发现其实内容在```<ul class="f-hide"></ul>```中
继续按部就班，把song id搞到
结果如下
```
{'等你下课 (with 杨瑞代)': '/song?id=531051217', '告白气球': '/song?id=418603077', '晴天': '/song?id=186016', '七里香': '/song?id=186001', '稻香': '/song?id=185709', '彩虹': '/song?id=185809',....
```

### 1.3 进入歌曲页，获取歌曲评论信息
