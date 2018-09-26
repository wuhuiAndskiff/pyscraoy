# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
"""
1.在items.py文件中，定义JobboleArticleItem类，需要基础scrapy的item。
2.在类中，具体定义爬虫的字段，指定为scrapy.Field，表示传递任何参数都可以，一共11个字段
添加原来就有的字段：标题，发布日期，点赞数，收藏数，评论数，标签，正文
添加封面url字段
如果封面图已经在本地保存，添加 本地存储的封面地址字段
添加博客url字段
因为现在的博客url字段时变长的，使用md5等压缩算法，添加 博客url定长字段。
3.现在item.py的代码如下：注意，Field() :  Field 后面 必须加 （），否则无法赋值
"""
class JobboleArticleItem(scrapy.Item):
    url = scrapy.Field() #博客url
    url_object_id =scrapy.Field() #url经过MD5等压缩成固定长度
    front_image_url = scrapy.Field() # 封面url
    front_image_path = scrapy.Field() # 本地存储的封面路径

    title = scrapy.Field()
    create_date = scrapy.Field()
    praise_nums= scrapy.Field()
    fav_nums= scrapy.Field()
    comment_nums= scrapy.Field()
    content= scrapy.Field()
    tag= scrapy.Field()