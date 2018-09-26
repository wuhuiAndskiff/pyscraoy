# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentcrawlPipeline(object):
    def __init__(self):
        self.filename=open("position.json","wb")

    def process_item(self, item, spider):
        # 将json对象转成json字符串存储到文件中
        text = json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.filename.write(text.encode("utf_8"))
        return item

    def close_spider(self):
        self.filename.close()