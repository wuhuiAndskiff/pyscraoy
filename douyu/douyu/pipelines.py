# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import  ImagesPipeline
import os

class DouyuPipeline(ImagesPipeline):
    #从配置文件中获取文件路径
   IMAGES_STORE =  get_project_settings().get("IMAGES_STORE")
   def get_media_requests(self, item, info):
        image_url = item['image_link']
        yield scrapy.Request(image_url)


   def item_completed(self, results, item, info):
        #ok和x都是results中的一个子集的属性，如果ok为true，则返回x['path']
        image_path = [x['path'] for ok,x in results if ok ]
        os.rename(self.IMAGES_STORE+"/"+image_path[0], self.IMAGES_STORE+"/"+ item['nick_name'] +".jpg")
        item['image_path'] = self.IMAGES_STORE + "/" +item['nick_name']
        return item


