# 拉勾全国数据分析岗位分析
标签（空格分隔）： Python 爬虫 数据分析

---

## 1. 项目背景
* 通过Python爬虫获取拉勾网上关于数据分析岗位的数据
* 对获取的数据进行清理
* 使用Pandas对数据进行分析，提出相关性建议
## 2. 数据获取
选用Python爬虫来获取拉勾网数据
### 2.1 遇到的一些问题
一开始按惯例右键审查元素查看源码，发现岗位信息包裹在```<div id="main container"><>```中，然而查看源码发现那部分代码是空的。经过搜索，得知拉勾网页采用了Ajax动态刷新的方式
F12 进入Network一探究竟
![此处输入图片的描述][1]
可以注意到一个Ajax.json页面，打开它，preview
![此处输入图片的描述][2]
好了，我需要的东西都在这里，而且它还直接就是Json格式
而我们需要的网址也发生了变化
```https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0```

---
好了，一切准备就绪，可以开始
还是Naive， 拉勾的反爬措施还是不错的，直接使用requests获取上面的网址的页面时，直接被拒绝，提示“您操作太频繁,请稍后再访问”，甚至一次都未成功。
继续搜索方法，结果[知乎的答案解决了问题](https://www.zhihu.com/question/63524231/answer/281876073), 将cookie中的JSESSIONID，user_trace_token 一些看起啦像随机生成的值替换成uuid，结果一次成功
```
def get_uuid():
    return str(uuid.uuid4())


def get_lagou(page):
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"

    querystring = {
        "px": "new",
        "city": "全国",
        "needAdditionalResult": "false",
        "isSchoolJob": "0"
    }

    payload = "first=false&pn=" + str(page) + "&kd=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90"
    cookie = "JSESSIONID=" + get_uuid() + ";" \
            "user_trace_token=" + get_uuid() + "; LGUID=" \
             + get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; " \
            "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' \
             '_ga=GA1.2.952298646.1514043316; ' \
             'LGSID=' + get_uuid() + "; " \
            "LGRID=" + get_uuid() + "; "

    headers = {
        'cookie': cookie,
        'origin': "https://www.lagou.com",
        'x-anit-forge-code': "0",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'referer': "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE?labelWords=&fromSearch=true&suginput=",
        'x-requested-with': "XMLHttpRequest",
        'connection': "keep-alive",
        'x-anit-forge-token': "None",
        'cache-control': "no-cache",
        'postman-token': "91beb456-8dd9-0390-a3a5-64ff3936fa63"
    }
    return requests.request("POST", url, data=payload, headers=headers, params=querystring).json()
```
2.2 把获取的内容导入到csv
```
def parse_url():
    contents = []
    for i in range(1, 30):
        content_json = get_lagou(i)['content']['positionResult']['result']
        for com in content_json:
            item = {'city': com['city'], 'companyFullName': com['companyFullName'],
                    'companyLabelList': com['companyLabelList'], 'companySize': com['companySize'],
                    'education': com['education'], 'financeStage': com['financeStage'], 'firstType': com['firstType'],
                    'industryField': com['industryField'], 'jobNature': com['jobNature'], 'latitude': com['latitude'],
                    'longitude': com['longitude'], 'positionAdvantage': com['positionAdvantage'],
                    'positionId': com['positionId'], 'positionLables': com['positionLables'],
                    'positionName': com['positionName'], 'salary': com['salary'], 'workYear': com['workYear']}
            contents.append(item)
    return contents
```
```
def parse_to_csv(contents):
    keys = contents[0].keys()
    with open('CONTENTS.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(contents)
```

---
新出现的问题，虽然拉勾页面总数是30，而实际上totalCount是2529，每页15条，那么应该有169页
```
pageCount = get_lagou(1)['content']['positionResult']['totalCount'] // 15
for i in range(1, pageCount + 1):
```
按照这个循环去爬取，还是有问题，最终结果是643变多了，但还是少了很多，于是决定将爬取过程打印下来看看发现了什么
```
for i in range(1, pageCount + 1):
        try:
            print("开始爬取第{}页".format(i))
            if i % 30 == 0:
                time.sleep(30)  # 每爬30页休息30秒
            content_json = get_lagou(i)['content']['positionResult']['result']
            for com in content_json:
                item = {'city': com['city'], 'companyFullName': com['companyFullName'],
                        'companyLabelList': com['companyLabelList'], 'companySize': com['companySize'],
                        'education': com['education'], 'financeStage': com['financeStage'],
                        'firstType': com['firstType'],
                        'industryField': com['industryField'], 'jobNature': com['jobNature'],
                        'latitude': com['latitude'],
                        'longitude': com['longitude'], 'positionAdvantage': com['positionAdvantage'],
                        'positionId': com['positionId'], 'positionLables': com['positionLables'],
                        'positionName': com['positionName'], 'salary': com['salary'], 'workYear': com['workYear']}
                contents.append(item)
            print("第{}页爬取完成！".format(i))
        except:
            print("Something happend!")
```
在这里发现每当爬取30页左右，就会出错，大概在爬取第60页时，又能正常爬取，这可能是爬取过于频繁，可以每爬取30页休息30s，成功解决
```
if i % 30 == 0:
    time.sleep(30)  # 每爬30页休息30秒
```

在将结果导入csv时，出现编码错误，解决方法
```
with codecs.open('lagou.csv', 'w', encoding="utf8") as f:
    dict_writer = UnicodeDictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(contents)
```
按此生成的csv用excel打开乱码，使用notepad++打开，转成utf8编码格式即可




## 3. 数据清理&数据分析


  [1]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/1.png
  [2]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/2.png