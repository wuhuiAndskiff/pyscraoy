# -*- coding: utf-8 -*-
import scrapy


class RenrencrawlSpider(scrapy.Spider):
    name = 'renrenCrawl'
    allowed_domains = ['www.renren.com']
    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url= url,
            formdata = {"email":"wuwnho@163.com","password":"wwh1105682468"},
            callback=self.parse_page
        )

    def parse_page(self, response):
        html  = open("demo.html","wb")
        print("=======================================================================================================")
        print(response.body)
        print("=======================================================================================================")
        html.write(response.body)
