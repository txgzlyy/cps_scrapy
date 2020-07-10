# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json
from elasticsearch import Elasticsearch

ES_HOST = 'http://220.171.100.22:43545'


class CpsBqgPipeline(object):
    def __init__(self):

        self.f = open('bqg.csv', 'w+', encoding="utf-8")
        # self.es = Elasticsearch([ES_HOST])

    def process_item(self, item, spider):

        # body = {
        #     "name": "凡人修仙传",
        #     'auther': "忘语",
        #     'capter': item.get("capter", 'xxx'),
        #     'txt': item.get("txt", 'xxx'),
        # }
        # print(body)
        # self.es.index(index="bqg_xiaosh", doc_type="doc", body=body, request_timeout=20)
        self.f.write(item.get("txt", 'xxx') + r"\n")
        # return item

    def close_spider(self, spider):

        self.f.close()
