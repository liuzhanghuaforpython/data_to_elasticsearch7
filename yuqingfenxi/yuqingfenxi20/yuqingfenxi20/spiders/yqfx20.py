# -*- coding: utf-8 -*-
import uuid

import scrapy
import time

from yuqingfenxi20 import settings
from yuqingfenxi20.items import Yuqingfenxi20Item
from yuqingfenxi20.spiders import ttomd


class Yqfx20Spider(scrapy.Spider):
    name = 'yqfx20'
    allowed_domains = ['http://www.bjnews.com.cn/']
    start_urls = ['http://www.bjnews.com.cn/realtime']
    #http://www.bjnews.com.cn/realtime?page=3
    for i in range(2, 10):
        start_urls.append("http://www.bjnews.com.cn/realtime?page={}".format(str(i)))

    def parse(self, response):

        url_list = response.xpath('//ul[@id="news_ul"]/li/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url = url,
                                 callback=self.parse_detail,
                                 dont_filter=True)

    def parse_detail(self,response):
        item = Yuqingfenxi20Item()
        id = str(uuid.uuid1())
        title = response.xpath('//h1/text()').extract_first()
        # releaseBy = '新京报'

        releaseTime = response.xpath('//div[@class="fl ntit_l"]/span[@class="date"]/text()').extract_first()
        source = '新京报'
        content_text = response.xpath('//div[@class="content"]/p//text()').extract()
        content_text = ''.join(content_text)
        detail = response.xpath('//div[@class="content"]/p').extract()
        # detail = ttomd.convert(''.join(detail)).replace('<br>\n','\n')
        detail = ''.join(detail)
        if "mp4" in detail:
            detail = ''
        if not detail:
            detail = ''
        pictures = response.xpath('//div[@class="content"]/p/img//@src').extract()
        if pictures:
            for picture in pictures:
                if 'http' not in picture:
                    pictures = []
                    detail = ''
                else:
                    pass
        else:
            pictures = []

        url = response.url
        tags = "快讯,头条"
        sourceType = 'Scrapy'
        isHot = 0
        version = settings.Version
        createTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        item['id'] = id
        item['title'] = title
        # item['releaseBy'] = releaseBy
        item['releaseTime'] = releaseTime
        item['source'] = source
        item['pictures'] = pictures
        item['detail'] = detail
        item['url'] = url
        item['content_text'] = content_text
        item['tags'] = tags
        item['sourceType'] = sourceType
        item['isHot'] = isHot
        item['version'] = version
        item['createTime'] = createTime
        if detail != '':
            yield item
