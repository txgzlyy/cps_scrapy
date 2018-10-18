# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from elasticsearch import Elasticsearch

ES_HOST = 'http://220.171.100.22:43545'


class CpsBqgPipeline(object):
    def __init__(self):
        # self.f = open('bqg.txt', 'w+')
        self.es = Elasticsearch([ES_HOST])

    def process_item(self, item, spider):

        body = {
            "name": item.get("name", 'xxx'),
            'new_capter': item.get("new_capter", 'xxx'),
            'auther': item.get("auther", 'xxx'),
            'capter': item.get("capter", 'xxx'),
            'txt': item.get("txt", 'xxx'),
        }
        print(body)
        self.es.index(index="bqg_xiaosh", doc_type="doc", body=body, request_timeout=20)
        print(123)
        return item

    def close_spider(self, spider):
        pass
        # self.f.close()
