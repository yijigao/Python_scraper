﻿# 拉勾全国数据分析岗位分析
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
<!-- ![此处输入图片的描述][1] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/1.jpg height="200" width="300">

可以注意到一个Ajax.json页面，打开它，preview

<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/2.jpg height="200" width="300">

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
### 2.2 爬取职位的详细信息
直接在岗位搜索页面是没有岗位具体信息的，需要点击进去
url大致是这么个格式
```https://www.lagou.com/jobs/3658927.html```,后面那串数字就是前面我们Json数据中的positionId
所以，思路是按前面的方法先获取一级页面，将positionId存入列表, 然后把positionId带入上面的网址取获取公司详情的页面,
还是要注意，频繁爬取会封禁ip，设置好延迟。

```
def get_positionId():
    positionId = []
    pageCount = get_first(1)['content']['positionResult']['totalCount'] // 15
    for i in range(1, pageCount+1 ):
        try:
            if i % 25 == 0:
                time.sleep(30)
            print("开始爬取第{}页...".format(i))
            content_json = get_first(i)['content']['positionResult']['result']
            for com in content_json:
                positionId.append(int(com['positionId']))
            print("成功获取第{}页的positionId!".format(i))
        except:
            print("Something happend!")
    return positionId


def get_content():
    contents = []
    for count, id in enumerate(get_positionId()):
        try:
            if (count+1) % 25 == 0:
                time.sleep(20)
            print("开始获取positionId={}的内容..{}".format(id, count))
            content = get_second(id)
            item = {
                "company": Selector(text=content).xpath("/html/body/div[2]/div/div[1]/div/div[1]/text()").extract()[0],
                "job_name": Selector(text=content).xpath("/html/body/div[2]/div/div[1]/div/span/text()").extract()[0],
                "salary": Selector(text=content).xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[1]/text()").extract()[
                    0].strip(),
                "city": Selector(text=content).xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[2]/text()").extract()[
                    0].strip('/').strip(),
                "work_year":
                    Selector(text=content).xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[3]/text()").extract()[
                        0].strip('/').strip(),
                "education":
                    Selector(text=content).xpath("/html/body/div[2]/div/div[1]/dd/p[1]/span[4]/text()").extract()[
                        0].strip('/').strip(),
                "job_description": Selector(text=content).xpath('//*[@id="job_detail"]/dd[2]/div').extract()[0]}
            contents.append(item)
            print("获取内容成功!")
        except:
            print("获取失败......")
    return contents
```

### 2.3 把获取的内容导入到csv
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

<!-- ![此处输入图片的描述][3] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/3.jpg height="200" width="500">

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
### 3.2 全国数据分析岗位薪资分布

<!-- ![此处输入图片的描述][4] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/a.jpg height="200" width="300">

全国数据分析岗位工作主要分布在10k-18k左右

### 3.3 哪些行业数据分析需求量大
```
# 行业分析
# 公司行业描述一般有两个词语，有的一个词语
fields = [str(field).replace("、", " ").replace(",", " ").split(" ") for field in lg_df.industryField]
def count_tags(fields):
    tags = {}
    for field in fields:
        for i in field:
            if i:
                if i not in tags:
                    tags[i] = 1
                else:
                    tags[i] += 1
    return tags
```

<!-- ![此处输入图片的描述][5] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/b.jpg height="200" width="300">

移动互联网以37.6%遥遥领先，其次是金融行业

### 3.4 城市 vs 岗位&薪资
#### 3.4.1 全国数据分析岗位分布

<!-- ![此处输入图片的描述][6] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/4.jpg height="200" width="300">

结果有点出乎意料，在北上广深四个一线城市中，北京的岗位数量远高于其他三个，而我目前所在的成都，岗位数量只有69，与一线城市相距甚远！
#### 3.4.2 不同城市数据分析薪资分布

<!-- ![此处输入图片的描述][7] ![此处输入图片的描述][8] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/5.jpg height="200" width="300">
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/6.jpg height="200" width="300">

从箱线图中可以得出结论：一线城市中北京依旧是工资最高的城市，不过，杭州表现也相当出色，排名第三，而杀入第五的厦门其实没有太大参考性，岗位数量太少。总之，数据分析师在北京、深圳、上海、杭州薪资还是可观的。

### 3.5 学历 vs 岗位&薪资
<!-- ![此处输入图片的描述][9] ![此处输入图片的描述][10] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/7.jpg height="200" width="300">
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/8.jpg height="200" width="300">

绝大多数公司要求本科以上学历，要求硕士甚至博士的公司真的很少，这次爬取的数据中，博士只有一家公司要求。
薪资方面，当然学历高有优势，但从箱线图来看优势其实不那么明显。

### 3.6 工作年限 vs 岗位&薪资
<!-- ![此处输入图片的描述][11] ![此处输入图片的描述][12] -->
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/9.jpg height="200" width="300">
<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/10.jpg height="200" width="300">

这里将应届毕业生，小于1年经验，不限经验的岗位合并在一起
1-3年和3-5年工作经验的数据分析师需求量最大，而不限年限的数据分析师岗位需求量还是有不少的。
薪资没什么好说的，工作年限越高，工资自然越高。

### 3.7 数据分析需要哪些技能
对于准备入行的新人来说，数据分析师需要哪些技能，新人该往哪些方向去学习还是很关键。
结合前面我已经获取了两千多家公司数据分析师的JD，来看看哪些技能是最需要的。

由于JD一般都有很多条，文字较多，这里可以采用Jieba来提取关键词，stopwords的话自己视情况多次尝试添加

先将所有文本保存至列表，并清理无效的字符
```
def remove_tags(description):
    tags = ['<p>', '</p>', '<div>', '</div>','<br>', '<p class="">']
    for tag in tags:
        description = description.replace(tag, "").strip()
    return description

job_df["job_description"] = job_df["job_description"].apply(remove_tags)

my_words = [word for word in job_df["job_description"]]
```

使用jieba分词，计算关键词频次
```
import jieba
import jieba.analyse

def count_tags(words):
    tags = {}
    for word in my_words:
        for tag in jieba.analyse.tfidf(word):
            if tag not in tags:
                tags[tag] = 1
            else:
                tags[tag] += 1
    return tags

jieba.analyse.set_stop_words(stop_words_path="stop_words.txt")
my_tags = count_tags(my_words)
```

来看看位于前列的关键词, 排名第一的是SQL, Python第三, 看来数据库是需求最高的技能
```
sorted(my_tags.items(), key=lambda a: a[1], reverse=True)[:50]
>>> output:
[('SQL', 960),
 ('SAS', 519),
 ('Python', 482),
 ('SPSS', 464),
 ('Excel', 419),
 ('统计学', 394),
 ('团队', 358),
 ('逻辑思维', 347),
 ('沟通', 320),
 ('互联网', 286),
 ('模型', 275),
 ('数据库', 248),
 ('PPT', 248),
 ('统计', 244),
 ('算法', 240),
 ('数据模型', 237),
 ('报告', 235),
 ('敏感度', 225),
 ('统计分析', 222),
 ('责任心', 215),
 ('业务部门', 214),
 ('海量', 208),
 ....
 ```

来做个词云
```
from wordcloud import WordCloud

word_cloud = WordCloud(font_path='C:\Windows\Fonts\Microsoft YaHei\msyh.ttc').fit_words(my_tags)
plt.imshow(word_cloud, aspect="auto")
plt.axis("off")
plt.show()
```

<img src=https://github.com/yijigao/Python_scraper/blob/master/lagou/libs/c.jpg height="400" width="500">

## 4. 总结

* 数据分析师总体薪资在10K-18K之间，80%岗位集中在北上广深，其中43%在北京，其他城市需求不高。 岗位主要集中在移动互联网(38%)，金融领域(15%)。
* 薪资方面一线城市中北京最高，其他三个一线城市差别不大
* 关于学历，84%公司要求本科以上学历，要求硕士、博士以上学历的公司仅5%。 薪资方面本科硕士相差不大
* 关于工作经验，80%以上公司需要的是1年以上工作经验，只有约13%的公司明确接受应届生或1年以下工作经验。薪资随工作经验而升高
* 主要所需技能：SQL, SAS, Python, SPSS, Excel
