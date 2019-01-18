# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Selector
from dianying.items import DianyingItem
from time import sleep

class Www80sSpider(CrawlSpider):
    name = 'www80s'
    allowed_domains = ['www.80s.tw']
    start_urls = ['https://www.80s.tw/movie/list']

    rules = (
        Rule(LinkExtractor(allow=r'movie/\d+'),
            follow=True),
        Rule(LinkExtractor(allow=r'movie/\d+'),
             callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        a=DianyingItem()
        print(response)
        data = Selector(response)
        a['x']=data.xpath('//head/title/text()').re('(.+)')
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        sleep(10)
        return a
