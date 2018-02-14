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
### 2.2 把获取的内容导入到csv
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
ok, 已经拿到数据了，打开jupyter notebook,准备用pandas来进行数据处理。
先来看看数据信息
```
lg_df = pd.read_csv("lagou.csv")
lg_df.info()
>>>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2505 entries, 0 to 2504
Data columns (total 17 columns):
city                 2505 non-null object
companyFullName      2505 non-null object
companyLabelList     2505 non-null object
companySize          2504 non-null object
education            2505 non-null object
financeStage         2504 non-null object
firstType            2505 non-null object
industryField        2504 non-null object
jobNature            2505 non-null object
latitude             2493 non-null float64
longitude            2493 non-null float64
positionAdvantage    2505 non-null object
positionId           2505 non-null int64
positionLables       2505 non-null object
positionName         2505 non-null object
salary               2505 non-null object
workYear             2505 non-null object
dtypes: float64(2), int64(1), object(14)
memory usage: 332.8+ KB
```
一共有2505个观测值，这个与我在拉勾网页上得到的内容很相近了
数据完整新较好，有部分变量有缺失值，但这些变量并不是很重要。
大概看看数据是啥样的？
```
lg_df.head()
>>> output:
```
![此处输入图片的描述][3]
### 3.1 处理薪资数据
从上图可以看到，薪资数据显示的是“10k-15k”这样的格式，这是个离散型数据，我需要将其转成连续的数值，这样才能进一步分析
主要思路，提取出数字，然后取平均值, 使用pandas的apply函数可以处理所有的薪资数据
```
# 处理薪资数据，将其转成具体数据取平均
def parse_salary(salary):
    if "-" in salary:
        salary = salary.replace("k", "").replace("K", "")
    else:
        salary = salary.split("k")[0]
    try:
        min_s = salary.split("-")[0]
        max_s = salary.split("-")[1]
        return ((int(min_s) + int(max_s)) * 1000) / 2
    except IndexError:
        return int(salary) * 1000

lg_df["salary_sp"] = lg_df["salary"].apply(parse_salary)
```
### 3.2 城市 vs 岗位&薪资
#### 3.2.1 全国数据分析岗位分布
![此处输入图片的描述][4]
结果有点出乎意料，在北上广深四个一线城市中，北京的岗位数量远高于其他三个，而我目前所在的成都，岗位数量只有69，与一线城市相距甚远！
#### 3.2.2 不同城市数据分析薪资分布
![此处输入图片的描述][5] ![此处输入图片的描述][6]
从箱线图中可以得出结论：一线城市中北京依旧是工资最高的城市，不过，杭州表现也相当出色，排名第三，而杀入第五的厦门其实没有太大参考性，岗位数量太少。总之，数据分析师在北京、深圳、上海、杭州薪资还是可观的。

### 3.3 学历 vs 岗位&薪资
![此处输入图片的描述][7] ![此处输入图片的描述][8]
绝大多数公司要求本科以上学历，要求硕士甚至博士的公司真的很少，这次爬取的数据中，博士只有一家公司要求。
薪资方面，当然学历高有优势，但从箱线图来看优势其实不那么明显。

### 3.4 工作年限 vs 岗位&薪资
![此处输入图片的描述][9] ![此处输入图片的描述][10]
这里将应届毕业生，小于1年经验，不限经验的岗位合并在一起
1-3年和3-5年工作经验的数据分析师需求量最大，而不限年限的数据分析师岗位需求量还是有不少的。
薪资没什么好说的，工作年限越高，工资自然越高。

  [1]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/1.jpg
  [2]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/2.jpg
  [3]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/3.jpg
  [4]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/4.jpg
  [5]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/5.jpg
  [6]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/6.jpg
  [7]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/7.jpg
  [8]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/8.jpg
  [9]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/9.jpg
  [10]: https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/10.jpg