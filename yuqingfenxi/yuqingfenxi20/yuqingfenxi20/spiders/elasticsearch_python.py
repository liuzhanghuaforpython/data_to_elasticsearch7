# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch_dsl import Document, Date, Integer, Keyword, Text, Completion, connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class ArticleType(Document):
    #文章类型
    suggest = Completion(analyzer="ik_max_word")
    #text类型自动分词，keyword不分词，ik_max_word最细度分词
    id = Keyword()
    title = Text(analyzer="ik_max_word")
    releaseTime = Date()
    url = Keyword()
    source = Keyword()
    pictures = Keyword()
    sourceType = Keyword()
    isHot = Integer()
    version = Integer()
    tags = Text(analyzer="ik_max_word")
    detail = Text(analyzer="ik_max_word")
    content_text = Text(analyzer="ik_max_word")
    createTime = Date()
    #创建索引为 baidu 的搜索引擎，分片数为5，副本数为1
    class Index:
        name = 'xinjingbao'
        settings = {
          "number_of_shards": 5,
          "number_of_replicas": 1,
        }
# create the mappings in elasticsearch


if __name__ == "__main__":
    ArticleType.init()
