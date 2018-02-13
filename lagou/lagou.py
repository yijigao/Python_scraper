# -*- coding:utf8 -*-
import csv
import uuid
import requests
import codecs
import time


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
    return requests.request("POST", url, data=payload, headers=headers, params=querystring).json(encoding='utf-8')


def parse_url():
    contents = []
    pageCount = get_lagou(1)['content']['positionResult']['totalCount'] // 15
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

    return contents


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v if isinstance(v, bytes) else v) for k, v in row.items()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def parse_to_csv(contents):
    # head = ['city', 'companyFullName', 'companyLabelList', 'companySize', 'education', 'financeStage',
    #         'firstType', 'industryField', 'jobNature', 'latitude', 'longitude', 'positionAdvantage',
    #         'positionId', 'positionLables', 'positionName', 'salary', 'workYear']
    print("正在写入csv......")
    keys = contents[0].keys()
    with codecs.open('lagou.csv', 'w', encoding="utf8") as f:
        dict_writer = UnicodeDictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(contents)
    f.close()
    print("csv 写入完成！")


if __name__ == "__main__":
    parse_to_csv(parse_url())
    # pageCout = get_lagou(1)['content']['positionResult']['totalCount'] // 15
    # print(pageCout)
