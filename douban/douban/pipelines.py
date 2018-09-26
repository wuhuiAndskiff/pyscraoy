# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        table_name = settings['MONGODB_TABLE_NAME']
        client = pymongo.MongoClient(host=host, port=port);
        # 获取指定的数据库
        mongodb = client[db_name]
        # 获取指定的数据库表
        self.table = mongodb[table_name]

    def process_item(self, item, spider):
        print("-"*120)
        data = dict(item)
        # 向数据库表中插入数据
        self.table.insert(data)
        return item
