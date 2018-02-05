# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Scrapy.lagou.lagou.items import LagouItem

class DaInLagouSpider(scrapy.Spider):
    name = 'DA_in_lagou'
    allowed_domains = ['https://www.lagou.com']

    # 建立需要爬取信息的url列表
    baseUrl = "https://www.lagou.com/"

    rules = (
        # https://www.lagou.com/gongsi/j9891.html follow 表示深度解析，即当前所有子页面
        Rule(LinkExtractor(allow=r'gongsi/j\d.html',), follow=True),
        # https://www.lagou.com/zhaopin/Java/?labelWords=label
        Rule(LinkExtractor(allow=r'zhaopin/.*',), follow=True),
        # https://www.lagou.com/jobs/2785439.html 如果当前url是jobs/\d+.html格式, 则回调parse_item进行具体的解析动作
        Rule(LinkExtractor(allow=r'jobs/\d+.html',), callback='parse_item', follow=True)
    )
    def parse(self, response):
        # collect "item_urls"
        items = []
        position = response.xpath('//*[@id="s_position_list"]')
        positionId = position.xpath('//@data-positionid').extract()
        for id in positionId:
            pass



