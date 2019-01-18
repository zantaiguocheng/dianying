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
            '//div/a[contains(text(),"尾页")]/@href').re('\d+')[0])+1
        for i in range(2, 4):
            yield Request(url='https://www.80s.tw/movie/list/-----p/'+str(i), callback=self.mvlink)

    def mvlink(self, response):
        links_rule = LinkExtractor(allow='/movie/\d+')
        links = links_rule.extract_links(response)
        for i in links:
            sleep(1)
            yield Request(i.url, callback=self.neirong)

    def neirong(self, response):
        data = Selector(response)
        itme = DianyingItem()
        itme['moviename'] = data.xpath(
            '//h1[@class="font14w"]/text()').extract()
        itme['jianjie'] = ''.join(data.xpath(
            '//div[@class="info" and child::h1[@class="font14w"]]/span/text()')[0:2].extract()).strip()
        itme['actor'] = data.xpath(
            '//span/a[contains(@href,"actor")]/text()').extract()
        itme['kind'] = data.xpath(
            '//span/a[contains(@href,"----")]/text()').extract()
        itme['country'] = data.xpath(
            '//span[child::span[contains(text(),"地区")]]/a/text()').extract()
        itme['language'] = data.xpath(
            '//span[child::span[contains(text(),"语言")]]/a/text()').extract()
        itme['daoyan'] = data.xpath(
            '//span/a[contains(@href,"dir")]/text()').extract()
        itme['sysj'] = data.re('上映日期：.*?(\d{4}-\d{2}-\d{2})')
        itme['pc'] = data.re('片长：\D+?(\d+[\u4E00-\u9FA5]+)')
        itme['gxsj'] = data.re('更新日期：.*?(\d{4}-\d{2}-\d{2})')
        itme['jqjs'] = ''.join(data.xpath(
            '//div[@id="movie_content"]/text()').extract()).strip()
        itme['dbpf'] = data.xpath(
            '//span[child::span[contains(text(),"豆瓣评分")]]/text()').re('\d+.\d+')
        downlink = data.xpath(
            '//div[@id="cpdl2list"]//a[@rel="nofollow"]/@href').extract()
        downlink_2 = data.xpath('//input[@class="checkone"]/@value').extract()
        for i in downlink_2:
            downlink.append(i)
        itme['downlink'] = downlink
        print(itme)
        return itme
