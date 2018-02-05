# -*- coding: utf-8 -*-
import scrapy


# 将需要爬的项目引入进来


class DemoSpider(scrapy.Spider):
    # 该爬虫的名字
    name = 'demo'

    # 规定爬虫爬取网页的域名
    allowed_domains = ['zimuku.net']

    # 开始爬取的url链接
    start_urls = ['http://zimuku.net/']

    def parse(self, response):
        """
        parse() 函数接收Response参数，就是网页爬取后返回的数据
        用于处理响应，它负责解析爬取的内容
        生成解析结果的字典， 并返回新的需要爬取的请求
        """

        # 爬取第一个字幕的名字
        name = response.xpath('//b/text()').extract()[1]

        # 建立一个item字典， 用于保存我们爬取到的结果，并返回给pipline处理
        items = {'第一个': name}

        return items
