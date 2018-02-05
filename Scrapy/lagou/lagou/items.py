# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company = scrapy.Field()  # 公司
    city = scrapy.Field()  # 城市
    experience = scrapy.Field()  # 要求经验
    education = scrapy.Field()  # 学历
    salary = scrapy.Field()  # 薪水
    label = scrapy.Field()  # 职位标签
    responsibility = scrapy.Field()  # 岗位职责
    requirements = scrapy.Field()  # 岗位需求
