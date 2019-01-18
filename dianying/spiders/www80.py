# -*- coding: utf-8 -*-
from time import sleep

import scrapy
from scrapy import Request, Selector
from scrapy.linkextractor import LinkExtractor

from dianying.items import DianyingItem


class Www80Spider(scrapy.Spider):
    name = 'www80'
    allowed_domains = ['www.80s.tw']
    start_urls = ['https://www.80s.tw/movie/list']

    def parse(self, response):
        data = Selector(response)
        number = int(data.xpath(
            '//div[@class="pager"]/a/@href')[-1].re('/(\d+)')[0])+1
        for i in range(1, number):
            sleep(10)
            yield Request(url='https://www.80s.tw/movie/list/-----p/'+str(i), callback=self.mvlink)

    def mvlink(self, response):
        links_rule = LinkExtractor(allow='/movie/\d+')
        links = links_rule.extract_links(response)
        for i in links:
            sleep(10)
            yield Request(i.url, callback=self.neirong)

    def neirong(self, response):
        data = Selector(response)
        itme = DianyingItem()
        itme['moviename'] = data.xpath(
            '//h1[@class="font14w"]/text()').extract()
        itme['jianjie'] = data.xpath(
            '//div[@class="info"]/span/text()')[1].re('\S+')
        itme['actor'] = data.xpath(
            '//span/a[contains(@href,"actor")]/text()').extract()
        itme['kind'] = data.xpath(
            '//span/a[contains(@href,"----")]/text()').extract()
        itme.country = data.re('地区：.+\s+.+>([\u4E00-\u9FA5]+)')
        itme.language = data.xpath(
            '//span/a[contains(@href,"---")]/text()').re('([\u4E00-\u9FA5]语)+')
        itme.daoyan = data.xpath(
            '//span/a[contains(@href,"dir")]/text()').extract()
        itme.sysj = data.re('上映日期：.*?(\d{4}-\d{2}-\d{2})')
        itme.pc = data.re('片长：\D+?(\d+[\u4E00-\u9FA5]+)')
        itme.gxsj = data.re('更新日期：.*?(\d{4}-\d{2}-\d{2})')
