# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class MyspiderPipeline(object):
    # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        self.filename = open("teacher.json","wb+")

    # process_item方法是必须写的，用来处理item数据
    def process_item(self, item, spider):
        jsonText = json.dumps(dict(item), ensure_ascii=False)+ "\n"
        self.filename.write(jsonText.encode("utf-8"))
        print("================================================")
        print(jsonText)
        print("================================================")
        return item

    def close_spider(self,spider):
        self.filename.close();