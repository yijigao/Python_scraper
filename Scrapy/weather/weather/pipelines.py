# -*- coding: utf-8 -*-

import codecs
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3

import requests


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
