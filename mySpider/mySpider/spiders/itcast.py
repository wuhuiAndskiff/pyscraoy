# -*- coding: utf-8 -*-
import scrapy
from  mySpider.items import MyspiderItem
"""
scrapy genspider itcast "www.itcast.cn"命令执行，会自动生成当前文件，其实也可以自己手动新建这个文件


"""

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'
    # 爬取的范围url
    allowed_domains = ['www.itcast.cn']
    # 爬取的第一个url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']


    def parse(self, response):
        with open("teacher.html","wb+") as f:
            f.write(response.body)
            f.close();

        print(response.body)

        items = []
        result  = response.xpath('//div[@class="li_txt"]');
        for it in result:
            item = MyspiderItem();
            #将取出来的结果转成字符串
            name = it.xpath('h3/text()').extract()
            level = it.xpath("h4/text()").extract()
            introduce = it.xpath("p/text()").extract()
            item['name'] = name[0]
            item['level'] = level[0]
            item['introduce'] = introduce[0]
            # items.append(item)
            yield item
        # return items
