# -*- coding: utf-8 -*-
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
