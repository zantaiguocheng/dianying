# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DianyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #moviename 电影名字
    #jianjie 简介
    #moviename_agein 又名
    #acter 演员
    #kind 种类
    #language 语言
    #daoyan 导演
    #country 国家
    #sysj 上映时间
    #pc 片长
    #gxsj 更新时间
    #dbpf 豆瓣评分
    #jqjs 剧情介绍
    #downlink 下载链接
    moviename = scrapy.Field()
    jianjie = scrapy.Field()
    actor = scrapy.Field()
    kind = scrapy.Field()
    language = scrapy.Field()
    daoyan = scrapy.Field()
    country = scrapy.Field()
    sysj = scrapy.Field()
    pc = scrapy.Field()
    gxsj = scrapy.Field()
    dbpf = scrapy.Field()
    jqjs = scrapy.Field()
    downlink = scrapy.Field()
    
