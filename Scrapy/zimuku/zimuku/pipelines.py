# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 处理spider 爬到的内容

class ZimukuPipeline(object):
    def process_item(self, item, spider):
        # 打印爬取到的结果
        print(item)
        return item
