# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
# 爬取豆瓣前250的电影并保存到数据库中
class DoubanmovieSpider(scrapy.Spider):
    name = 'doubanmovie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = [url + str(offset)]

    def parse(self, response):
       for each in  response.xpath("//div[@class='info']"):
           item = DoubanItem()
           item['title'] = each.xpath(".//a/span[@class='title']/text()").extract()[0]
           item['info'] = each.xpath(".//div[@class='bd']/p/text()").extract()[0]
           item['star'] = each.xpath(".//div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()[0]
           item['introduce'] = each.xpath(".//p[@class='quote']/span[@class='inq']/text()").extract()[0]
           print("=======================================================================")
           print(item)
           print("=======================================================================")
           yield item
       self.offset += 25

       if self.offset <= 250:
        yield scrapy.Request(url=self.url+str(self.offset),callback=self.parse)

