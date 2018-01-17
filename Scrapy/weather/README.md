## 使用scrapy 爬取中国天气网天气数据

1. 数据的筛选
天气数据包裹在```<div class="weatherbox">``` 中
可以使用bs4, xpath, css 之类的选择器定位到这里，这次选用xpath
```
response.xpath('//div[@class = 'weatherbox']')
```
2. Scrapy 框架的实施
```
scarapy startproject weather
cd weather
scrapy gensipder ChengDu_weather http://www.tianqi.com/chengdu
```

3. 编写items, 只需将希望获取的字段填写进去
```
import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    week = scrapy.Field()
    img = scrapy.Field()
    temperature = scrapy.Field()
    weather = scrapy.Field()
    wind = scrapy.Field()
```

4. 编写Spider
这个部分是爬虫的核心
主要目的是：从Downloader发给我们的Response里筛选数据，并返回给PIPELINE处理
```
import scrapy

# 别忘了将item导入进来，这样数据才能在各个模块之间流转
from weather.items import WeatherItem


class ChengduWeatherSpider(scrapy.Spider):
    name = 'ChengDu_Weather'
    # 修改一下host, 使得scrapy可以爬取我们想要的城市的天气
    allowed_domains = ['https://www.tianqi.com']

    # 建立需要爬取信息的url列表
    start_urls = []

    # 需要怕的城市名称
    cities = ['chengdu', 'nanchang', 'ganzhou', 'shenzhen']

    # 生成需要爬取的链接

    for city in cities:
        start_urls.append('https://www.tianqi.com/' + city)

    def parse(self, response):
        """
        筛选信息
        """
        # 建立一个列表用于保存每天的信息
        items = []
        # 找到包裹每天天气信息的div
        days_of_seven = response.xpath('//div[@class="day7"]')

        for i in range(7):
            # 先申请一个weatheritem的类型来保存结果
            item = WeatherItem()
            date = days_of_seven.xpath('//ul[@class="week"]/li/b/text()').extract()[i]
            city = response.xpath('//dd[@class="name"]/h2/text()').extract()[0]
            item["date"] = city + " " + date + " 天气"
            item['week'] = days_of_seven.xpath('//ul[@class="week"]/li/span/text()').extract()[i]
            item['img'] = days_of_seven.xpath('//ul[@class="week"]/li/img/@src').extract()[i]
            item['weather'] = days_of_seven.xpath('//ul[@class="txt txt2"]/li/text()').extract()[i]
            temp1 = days_of_seven.xpath('//div[@class="zxt_shuju"]/ul/li/b/text()').extract()[i]
            temp2= days_of_seven.xpath('//div[@class="zxt_shuju"]/ul/li/span/text()').extract()[i]
            item['temperature'] = temp1 + "-" + temp2 + "℃"
            item['wind'] = days_of_seven.xpath('//ul[@class="txt"]/li/text()').extract()[i]

            items.append(item)

        return items
```


4. 编写Pepline
pepline.py用于处理爬取到的数据
一般有三种保存形式txt, json, sql

txt 格式
```
class WeatherPipeline(object):
    def process_item(self, item, spider):
        """
        处理每一个从ChengDu_Weather传过来的item
        """
        # 获取当前的工作目录
        base_dir = os.getcwd()
        # 文件存在data目录下的weather.txt 文件内
        filename = base_dir + '\\data\\weather.txt'

        # 从内存以追加的方式打开文件，并写入对应的数据
        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['wind'] + '\n\n')

        # 下载图片
        with open(base_dir + '/data/' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get(item['img']).content)

        return item
```

json格式
```
# 输出json 数据
class W2json(object):
    def process_item(self, item, spider):
        """
        将爬取的信息保存到json
        :param item:w
        :param spider:
        :return:
        """
        base_dir = os.getcwd()
        filename = base_dir + '\\data\\weather.json'

        # 打开json文件， 向里面以dumps的方式吸入数据
        # 注意需要有一个参数ensure_ascii=false, 不然会直接为utf编码的方式存入：
        with codecs.open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)

        return item
```

sql格式
```
class W2sql(object):
    def process_item(self, item, spider):
        """
        将爬取的信息保存到sql
        :param item:
        :param spider:
        :return:
        """
        date = item['date']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']
        img = item['img']

        # 建立数据库
        base_dir = os.getcwd()
        filename = base_dir + '\\data\\weather_cd.db'
        con = sqlite3.connect(filename)
        cur = con.cursor()
        try:
            # create table
            # cur.execute("""
            #   CREATE TABLE my_weather (
            #   date INTEGER,
            #   week INTEGER,
            #   temperature INTEGER,
            #   weather INTEGER,
            #   wind INTEGER,
            #   img INTEGER
            #   )
            # """)
            cur.execute("INSERT INTO my_weather VALUES (?,?,?,?,?,?)", (date, week, temperature, weather, wind, img))
            #提交本次插入记录
            con.commit()
        finally:
            # 关闭连接
            con.close()

        return item
```

