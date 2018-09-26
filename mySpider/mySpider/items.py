# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
"""
在这个文件中，写爬取的数据实体，即将数据放到MySiderItem来存储
"""
import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    introduce = scrapy.Field()

