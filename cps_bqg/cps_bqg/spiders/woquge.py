# -*- coding: utf-8 -*-
import scrapy
import time

from ..items import CpsBqgItem


class WoqugeSpider(scrapy.Spider):
    name = 'woquge'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/']

    # start_urls = ['https://www.woquge.com/2_2714/151901248.html']

    def start_requests(self):
        lists = ['http://www.xbiquge.la/19/19677/', 'http://www.xbiquge.la/5/5395/', 'http://www.xbiquge.la/0/215/',
                 'http://www.xbiquge.la/7/7416/', 'http://www.xbiquge.la/15/15977/']
        for _ in lists:
            print(_)
            yield scrapy.Request(_)

    def parse(self, response):
        tittle = response.xpath("//h1/text()").extract_first()
        capter_list = response.xpath("//div[@id='list']//dl//dd")
        for index, i in enumerate(capter_list):
            url = 'http://www.xbiquge.la' + i.xpath("./a/@href").extract_first()
            time.sleep(2)
            yield scrapy.Request(url, callback=self.get_txt, meta={"num": index, 'tittle': tittle})

    def get_txt(self, response):
        data = response.meta
        num = data.get('num') + 1
        tittle = data.get('tittle')
        print(num, '-------------------------------------------------------------------------')
        item = {}

        capter = response.xpath("//h1/text()").extract_first()
        txts = response.xpath("//div[@id='content']/text()").extract()
        strs = ''
        for i in txts:
            txt = i.strip()  # 去除空格
            strs = strs + txt
        item["num"] = num
        item["name"] = tittle
        item['auther'] = "忘语"
        item["capter"] = capter
        item["txt"] = strs
        yield item
