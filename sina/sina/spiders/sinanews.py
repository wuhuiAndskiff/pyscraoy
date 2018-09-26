# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem
import os

class SinanewsSpider(scrapy.Spider):
    name = 'sinanews'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        items = []
        # 所有大类的标题
        parentTitle=   response.xpath("//div[@class='clearfix']/h3/a/text()").extract()
        # 所有大类的url
        parentUrl  = response.xpath("//div[@class='clearfix']/h3/a/@href").extract()
        #所有的小标题
        subTitle = response.xpath("//div[@class='clearfix']/ul[@class='list01']//a/text()").extract()
        # 所有的小标题的url
        subUrl = response.xpath("//div[@class='clearfix']/ul[@class='list01']//a/@href").extract()

        print(parentUrl)

        # 爬取所有的大类
        for  i in range(0,len(parentUrl)):
            parentPtah = "/Data/"+ parentTitle[i]
            if(not os.path.exists(parentPtah)):
                # 新建大类文件夹
                os.mkdir(parentPtah)

            # 爬取所有的小类
            for j in range(0,len(subUrl)):
                item = SinaItem()
                item["parentTitle"] = parentTitle[i]
                item["parentUrl"] = parentUrl[i]

                # 判断子目录的起始url是否是以父目录的url一样
                isTheSameParentTitle = subUrl[j].startswith(item["parentUrl"])
                if(isTheSameParentTitle):

                    subFileName = parentPtah + "/" +subTitle[j]

                    if not os.path.exists(subFileName):
                        os.mkdir(subFileName)

                    item["subTitle"] = subTitle[j]
                    item["subUrl"] = subUrl[j]
                    item["subFileName"] = subFileName
                    items.append(item)


        for item in items:
            yield scrapy.Request(url=item["subUrl"],meta={"item_1":item},callback=self.sub_content_parse)


    # 爬取小类的url
    def sub_content_parse(self,response):
        resp_item = response.meta["item_1"]
        contents = ""
        # 获取所有的小类里面的文章的url
        sonUrls = response.xpath("//a/@href").extract()
        items  = []

        for k in range(0,len(sonUrls)):

             # 判断小类文章的url是否与大类起始url相同，并且是以shtml结尾的
            isSubLink = sonUrls[k].endswith(".shtml") and sonUrls[k].startswith(resp_item["parentUrl"])
            if isSubLink :
                item = SinaItem()
                item["parentTitle"] = resp_item["parentTitle"]
                item["parentUrl"] = resp_item["parentTitle"]
                item["subTitle"] = resp_item["subTitle"]
                item["subUrl"] = resp_item["subUrl"]
                item["subFileName"] = resp_item["subFileName"]
                item["sonUrl"] = sonUrls[k]
                items.append(item)



        # 针对过滤的url进行逐一的发送请求
        for item in items:
            yield scrapy.Request(url=item["sonUrl"], meta={"item_2":item}, callback=self.content_parse)


    # 解析小类中每一个url，即具体链接下的文章内容
    def content_parse(self,response):

        item  = response.meta["item_2"]
        content = ""
        title = response.xpath("//h1[@class='main-title']/text()").extract()

        # 该匹配的contents在段落里面的的内容，需要再次处理一下
        contents = response.xpath("//div[@class='article']//p/text()").extract()

        for cont in contents:
            content += cont


        item["title"] = title
        item["content"] = content
        print("-"*120)
        print(item)
        print("-"*120)

        yield item







