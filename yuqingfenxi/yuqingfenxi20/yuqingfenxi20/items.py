# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from yuqingfenxi20.spiders.elasticsearch_python import ArticleType
from w3lib.html import remove_tags
from elasticsearch_dsl.connections import connections

es = connections.create_connection(ArticleType)

def get_suggests(index,info_tuple):
    #根据字符串生成搜索建议数据
    used_words = set()
    suggests = []
    for text,weight in info_tuple:
        if text:
            words = es.indices.analyze(index="xinjingbao",
                                       body={"analyzer": "ik_max_word", "text": "{0}".format(text)})
            analyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"]) > 1])
            new_words = analyzed_words - used_words
        else:
            new_words = set()
        if new_words:
            suggests.append({"input":list(new_words),"weight":weight})
    return suggests


class Yuqingfenxi20Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    # 标题
    title = scrapy.Field()

    releaseBy = scrapy.Field()
    # #摘要
    # summary = scrapy.Field()
    # 细节详情
    detail = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    # 图片链接
    pictures = scrapy.Field()

    content_text = scrapy.Field()
    # 原始链接
    url = scrapy.Field()
    # 发布日期
    releaseTime = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 来源类型
    sourceType = scrapy.Field()

    isHot = scrapy.Field()

    version = scrapy.Field()
    # 爬虫时间
    createTime = scrapy.Field()

    def save_to_es(self):
        article = ArticleType()
        article.id = self["id"]
        article.title = self["title"]
        article.releaseTime = self["releaseTime"]
        article.url = self["url"]
        article.source = self["source"]
        if len(self["pictures"]) > 0:
            article.pictures = ';'.join(self["pictures"])
        article.sourceType = self["sourceType"]
        article.isHot = self["isHot"]
        article.tags = self["tags"]
        article.detail = remove_tags(self["detail"])
        article.content_text = self["content_text"]
        article.createTime = self["createTime"]
        article.suggest = get_suggests(ArticleType,((article.title,10),(article.tags,7)))
        article.save()
        return
