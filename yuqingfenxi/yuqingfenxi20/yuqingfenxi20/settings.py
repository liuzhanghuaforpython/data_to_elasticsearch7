# -*- coding: utf-8 -*-

# Scrapy settings for yuqingfenxi20 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yuqingfenxi20'

SPIDER_MODULES = ['yuqingfenxi20.spiders']
NEWSPIDER_MODULE = 'yuqingfenxi20.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'yuqingfenxi20.middlewares.Yuqingfenxi20SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'yuqingfenxi20.middlewares.Yuqingfenxi20DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'yuqingfenxi20.pipelines.ElasticSearchPipeline': 300,
}

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
# Kafka
# KAFKA_HOST='kafka1.flagnw.net:9092,kafka2.flagnw.net:9092,kafka3.flagnw.net:9092,10.1.150.1:9092,10.1.150.2:9092,10.1.150.3:9092'
# KAFKA_HOST='10.103.11.1:9092,10.103.11.2:9092,10.103.11.3:9092'
# KAFKA_TOPIC='spiderPublicOpinionOriginal'
#
Version = 1
#
# # 全量爬取还是增量爬取，如果是0 表示全量爬取，如果是1 ，表示增量爬取
# # SCRAPY_TYPE='1'
#
# # # 不重试
# RETRY_ENABLED = False
# # 超时时间
# DOWNLOAD_TIMEOUT = 10
# # 设置延迟下载可以避免被发现
# DOWMLOAD_DELAY = 2
# # 在高延迟的情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 5
# DB_HOST = 'localhost'
# DB_PORT = 3306
# DB_USER = 'root'
# DB_PWD = 'root'
# DB_NAME = 'yuqingshuju'
# DB_CHARSET = 'utf8'