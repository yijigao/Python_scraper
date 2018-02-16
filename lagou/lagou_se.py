# 爬取二级页面

import requests
import uuid
from scrapy import Selector
from pprint import pprint
import time
import csv
import codecs


def get_uuid():
    return str(uuid.uuid4())


def get_first(page):
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


def get_second(positionId):
    url = "https://www.lagou.com/jobs/{}.html".format(positionId)
    cookie = "_ga=GA1.2.52116706.1518422697; \
            _gid=GA1.2.316199249.1518422697;\
             user_trace_token={}; \
             LGUID={}; \
             index_location_city=%E5%85%A8%E5%9B%BD; \
             showExpriedIndex=1; \
             showExpriedCompanyHome=1; \
             showExpriedMyPublish=1; \
             hasDeliver=9; \
             JSESSIONID={}; \
             _putrc=D7D872B68D97AD60; \
             login=true; unick=%E6%98%93%E7%BB%A7%E9%AB%98; \
             Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518516255,1518516562,1518594538,1518608629;\
             TG-TRACK-CODE=search_code; \
             SEARCH_ID={}; \
             _gat=1; \
             LGSID={}; \
             PRE_UTM=; PRE_HOST=; PRE_SITE=; \
             PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F4076639.html; \
             LGRID={}; \
             Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1518616323; \
             gate_login_token={}".format(get_uuid(), get_uuid(), get_uuid(), get_uuid(), get_uuid(), get_uuid(),
                                         get_uuid())
    headers = {
        "cookie": cookie,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=30)
    return r.text


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
    with codecs.open('LG.csv', 'w', encoding="utf8") as f:
        try:
            dict_writer = UnicodeDictWriter(f, ['company', 'job_name', 'salary', 'city', 'work_year', 'education',
                                                'job_description'])
            dict_writer.writeheader()
            dict_writer.writerows(contents)
            f.close()
            print("csv 写入完成！")
        except:
            print("妈卖批，写入出错啦...")


if __name__ == "__main__":
    parse_to_csv(get_content())
