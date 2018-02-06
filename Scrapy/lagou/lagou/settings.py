# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html




BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     "Accept": "application/json, text/javascript, */*; q=0.01",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh,zh-CN;q=0.9,ja;q=0.8,en-GB;q=0.7,en;q=0.6,en-US;q=0.5",
#     "Connection": "keep-alive",
#     "Content-Length": "55",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "Cookie": "user_trace_token=20171221173655-bad81cc8-b220-40d6-a680-6a977b89a321; _ga=GA1.2.1354272760.1513849017; LGUID=20171221173656-7bf21798-e632-11e7-9dfc-5254005c3644; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; _gid=GA1.2.728225229.1517837412; hasDeliver=5; index_location_city=%E5%85%A8%E5%9B%BD; LGSID=20180206205930-91c4acde-0b3d-11e8-bc1e-525400f775ce; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0xfb31bd3300039750%26issp%3D1%26f%3D3%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D3%26rsv_sug7%3D100%26rsv_sug2%3D0%26prefixsug%3Dla%26rsp%3D0%26inputT%3D1720%26rsv_sug4%3D2257; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_cd_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517648145,1517744713,1517837412,1517921976; _putrc=D7D872B68D97AD60; JSESSIONID=ABAAABAAAIAACBI481D920FAB459A6FA5EE2513B711A2B7; login=true; unick=%E6%98%93%E7%BB%A7%E9%AB%98; gate_login_token=dc5c4031b3a89552291adde5f3ff4febafa5ecae9e8b7748; TG-TRACK-CODE=search_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517922505; LGRID=20180206210819-cd2594f1-0b3e-11e8-af7a-5254005c3644; SEARCH_ID=f3e9c9170b244f238ebf9320bcfef03b",
#     "DNT": "1",
#     "Host": "www.lagou.com",
#     "Origin": "https://www.lagou.com",
#     "Referer": "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
#     "X-Anit-Forge-Code": "0",
#     "X-Anit-Forge-Token": "None",
#     "X-Requested-With": "XMLHttpRequest"
# }
#

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.LagouDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lagou.pipelines.LagouPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
