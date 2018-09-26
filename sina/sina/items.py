# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # 父目录名称
    parentTitle = scrapy.Field()
    parentUrl = scrapy.Field()

    # 子目录
    subTitle = scrapy.Field()
    subUrl = scrapy.Field()
    # 子目录的文件路径
    subFileName = scrapy.Field()
    #子目录下的文章链接
    sonUrl = scrapy.Field()



    # 文章标题
    title = scrapy.Field()
    # 文章内容
    content = scrapy.Field()


