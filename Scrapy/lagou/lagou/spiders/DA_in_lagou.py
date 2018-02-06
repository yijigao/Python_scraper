# -*- coding: utf-8 -*-
import json
import uuid
import requests

import scrapy


class DaInLagouSpider(scrapy.Spider):
    name = 'DA_in_lagou'
    allowed_domains = ['https://www.lagou.com']

    # 建立需要爬取信息的url列表
    start_urls = (
        "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0",
    )

    def parse(self, response):
        # collect "item_urls"
        jdict = json.loads(response.body)
        print(jdict)
        # jresult = jcontent['result']
        # for each in jresult:
        #     print(each['city'])
        #     print(each['companyName'])
        #     print(each['companySize'])
        #     print(each['positionName'])
        #     print(each['positionType'])
        #     print(each['salary'])
        #     print()
