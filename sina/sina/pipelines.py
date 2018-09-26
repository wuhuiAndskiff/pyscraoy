# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        sonUrl = item["sonUrl"]

        # 将下载的html文件重命名,http://news.sina.com.cn/c/2018-09-19/doc-ifxeuwwr5935765.shtml,去除http://和后缀.shtml
        fileName = sonUrl[7:-6].replace("/","-") + ".txt"

        sonFile = open(item["subFileName"]+"/"+fileName,"wb")
        sonFile.write(item["content"].encode('utf8'))
        sonFile.close()
        return item
