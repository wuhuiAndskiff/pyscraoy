# -*- coding: utf-8 -*-
import scrapy
# 导入链接匹配类，用于匹配符合规则的链接
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencentcrawl.items import TencentItem


class TencentSpider(CrawlSpider):
    name = "tencent"
    allow_domains = ["hr.tencent.com"]
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    page_link = LinkExtractor(allow="start=\d+")
    # 匹配的规则
    rules = (
        # allow满足的正则表达式，callback:回调请求的方法，注意这个是字符串，这个字符串是回调函数名
        Rule(page_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        item_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for each in item_list:
            # 职位名
            item = TencentItem()
            item['position_name'] = each.xpath("./td[1]/a/text()").extract()[0]
            # 详情连接
            item['position_link'] = each.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            item['position_type'] = each.xpath("./td[2]/text()").extract()[0]
            # 招聘人数
            item['people_num'] = each.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            item['work_location'] = each.xpath("./td[4]/text()").extract()[0]
            # 发布时间
            item['publish_time'] = each.xpath("./td[5]/text()").extract()[0]
            yield item

