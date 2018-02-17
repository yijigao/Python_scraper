import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from scrapy import Selector

headers = {
    "Accept": "text/html, application / xhtml + xml, application / xml;\
                  q = 0.9, image / webp, image / apng, * / *;q = 0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh,zh-CN;q=0.9,ja;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5",
    "Connection": "keep-alive",
    "Cookie": "_iuqxldmzr_=32;"
              " _ntes_nnid=773f2853ee69df661e6a4972f27f4726,1517319989559;"
              " _ntes_nuid=773f2853ee69df661e6a4972f27f4726;"
              " __utmz=94650624.1517319990.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;"
              " __utmc=94650624; "
              "JSESSIONID-WYYY=3Vwm8JIRVqlPdhzItnI6H4xeKG93m1N7Z0g1PZDBJ86orZsYA35yYJTDTC6swEk%5CXmzE1JFRt4N%2FThvUAAIWNgqBnbRjp%2FvzEvagFYvXcqIeq6%5CumvvarXQIzFtWWh%2BoOBzssbv0izoXyH0XpAuJYEDPYY0uFgd3o4SPaGFQ78SD8yye%3A1518870790654;"
              " __utma=94650624.349500884.1517319990.1518862029.1518869311.3;"
              " __utmb=94650624.2.10.1518869311 ",
    "DNT": "1",
    "Host": "music.163.com",
    "Referer": "http://music.163.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/64.0.3282.167 Safari/537.36"
}


def get_first_html(url, headers):
    r = requests.request("GET", url=url, headers=headers)
    return r.text


def get_second_html(artist_id, headers):
    url = "http://music.163.com" + artist_id
    r = requests.request("GET", url=url, headers=headers)
    return r.text


def get_third_html(song_id, headers):
    url = "http://music.163.com" + song_id
    r = requests.request("GET", url=url, headers=headers)
    return r.text


def get_artist_id(response):
    soup = BeautifulSoup(response, "lxml")
    sel = soup.find(class_="m-sgerlist")
    s_dict = {}
    for ele in sel.find_all('a'):
        if ele.text:
            s_dict[ele.text] = ele.get('href')
    return s_dict


def get_song_id(response):
    soup = BeautifulSoup(response, "lxml")
    sel = soup.find(class_='f-hide')
    song_dict = {}
    for el in sel.find_all("a"):
        song_dict[el.text] = el.get("href")
    print(song_dict)


def get_song_content(response):
    soup = BeautifulSoup(response, "lxml")
    # 歌词信息
    lyric = soup.find(id="lyric-content")
    print(lyric)


if __name__ == "__main__":
    url = "http://music.163.com/discover/artist/cat?id=1001"
    get_song_content(get_third_html("/song?id=531051217", headers))
