# -*- coding: utf-8 -*-

# Scrapy settings for ZhihuUser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ZhihuUser'

SPIDER_MODULES = ['ZhihuUser.spiders']
NEWSPIDER_MODULE = 'ZhihuUser.spiders'

MONGO_URI = 'localhost'
MONGO_DB = 'ZhihuUser'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ZhihuUser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'cookie': '_zap=63a9fc25-553a-4a13-a25f-b78128c666f5; d_c0="AHCuhl9WkQ2PTqpYktodSaphaOJTSGDSpG0=|1525871726"; _xsrf=s5fA7OpRwm6tGc61t1ZgZF9FiF1uInB9; q_c1=deb2f784ec0d404d8ad010e8d1ac5cac|1533818231000|1533818231000; l_n_c=1; n_c=1; __utmc=155987696; __utmz=155987696.1535464391.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=155987696.2016362934.1535464391.1535497982.1535542604.3; capsion_ticket="2|1:0|10:1537445723|14:capsion_ticket|44:Mjc5OTg5NjQ0MTU1NGExMzgzOWUyYjdjODhiN2Q0ZjU=|d7af09a355e9d8b5bc84b8b0b7a60b7e3f3a9b67e2c0c1e51aa66da6fbb921b8"; tgw_l7_route=e0a07617c1a38385364125951b19eef8; anc_cap_id=0935b573b3a046aeb1b71cad44b5d678; l_cap_id="OTJlY2ViZTRjNTFmNDE5OGE3NWY4ZGMyNjUzNWYyNDA=|1537449615|4b0d0f11a3dbe6d31eef68d7ca89b3af7e3bb5da"; r_cap_id="NGU5ZmYwYjhlMjRhNGQ2NGIyNzU2NWRhNDY4YzMyY2M=|1537449615|43c520bb04cc0f5eeaf6b6c71ce14f7b955ad857"; cap_id="OTk3YjE4ZGJjNDQ3NGVlNmJkYWYzODE3YjI2MmU4MjY=|1537449615|c70ec560c1cb8f77121a3511890f4f88744e2d5e',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ZhihuUser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ZhihuUser.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ZhihuUser.pipelines.MongoPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

REDIS_URL = "redis://root:qingyunke@132.232.170.116:6379"