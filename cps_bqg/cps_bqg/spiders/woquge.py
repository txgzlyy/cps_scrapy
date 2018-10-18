# -*- coding: utf-8 -*-
import scrapy

from ..items import CpsBqgItem


class WoqugeSpider(scrapy.Spider):
    name = 'woquge'
    allowed_domains = ['woquge.com']
    start_urls = ['https://www.woquge.com/xiuzhenxiaoshuo/']
    # start_urls = ['https://www.woquge.com/2_2714/151901248.html']

    def parse(self, response):
        xiaoshuos = response.xpath("//div[@id='newscontent']//li")
        print(123)
        for i in xiaoshuos:
            data = {}

            name = i.xpath("./span[@class='s2']//a/text()").extract_first()
            new_capter = i.xpath("./span[@class='s3']//a/text()").extract_first()
            auther = i.xpath("./span[@class='s5']/text()").extract_first()

            data['name'] = name
            data['new_capter'] = new_capter
            data['auther'] = auther
            # yield item
            url = 'https://www.woquge.com' + i.xpath("./span[@class='s2']//a/@href").extract_first()
            # print(url)
            yield scrapy.Request(url, callback=self.get_xiaoshuo, meta={"data": data, 'base_url': url})

    def get_xiaoshuo(self, response):
        data = response.meta['data']
        base_url = response.meta['base_url']
        capters = response.xpath("//div[@id='list']//dd//a")
        for i in capters:
            url = base_url + i.xpath("./@href").extract_first()
            print(url)
            yield scrapy.Request(url, callback=self.get_txt, meta={"data": data})

    def get_txt(self, response):
        data = response.meta['data']
        item = {}

        capter = response.xpath("//h1/text()").extract_first()
        txts = response.xpath("//div[@id='content']//p")
        strs = ''
        for i in txts:
            txt = i.xpath('./text()').extract_first().lstrip()  # 去除左边空格
            strs = strs + txt

        item['name'] = data['name']
        item['new_capter'] = data['new_capter']
        item['auther'] = data['auther']
        item["txt"] = strs
        item["capter"] = capter
        yield item
