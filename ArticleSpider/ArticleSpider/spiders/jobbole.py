# -*- coding: utf-8 -*-
import scrapy
import  re
from scrapy.http import  Request
from urllib import parse
from ArticleSpider.items import JobboleArticleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/107275/']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    def parse(self, response):
        """
        1.获取文章列表页中的文章url,并交给scrapy下载后并进行解析
        2.获取下一页的URL并交给scrapy进行下载，下载完成后交给parse
        """
        #获取文章列表页中的文章url,并交给scrapy下载后并进行解析
        post_urls = response.css('#archive .floated-thumb .post-thumb a::attr(href)').extract()
        for post_url in post_urls:
            yield Request(url = parse.urljoin(response.url, post_url),callback = self.parse_detail)

        #提取下一页URL，并交给scrapy进行下载
        next_url = response.css(".next.page-numbers ::attr(href)").extract_first("")
        if next_url:
            yield Request(url= parse.urljoin(response.url,next_url), callback=self.parse)

    def parse(self, response):

        post_urls = response.css('#archive .floated-thumb .post-thumb a::attr(href)').extract()
        # 使用CSS选择器
        # 标题
        title = response.css('.entry-header h1::text').extract()[0]
        # 发表日期
        create_date = response.css('.entry-meta-hide-on-mobile ::text').extract()[0].strip().replace("·", "").strip()
        # 点赞数
        praise_nums = response.css('.vote-post-up h10::text').extract()[0]
        match_re = re.match('.*?(\d+).*', praise_nums)
        if match_re:
            praise_nums = int(match_re.group(1))
        else:
            praise_nums = 0
        # 收藏数
        fav_nums = response.css('.bookmark-btn::text').extract()[0]
        match_re = re.match('.*?(\d+).*', fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0
        # 评论数
        comment_nums = response.css('a[href="#article-comment"] span ::text').extract()[0]
        match_re = re.match('.*?(\d+).*', comment_nums)
        if match_re:
            comment_nums = int(match_re.group(1))
        else:
            comment_nums = 0

            """
            extract()[0] 优化：
            对于确定使用  extract()[0] 的时候，可以用  extract_first()  替换
             extract_first() 取空值时，会返回一个默认值，默认值可在 () 中指定 "" 为空，而不用抛出异常
            """
        # 正文
        content = response.css('.entry').extract()[0]
        # 标签
        tag_list = response.css('.entry-meta-hide-on-mobile a ::text').extract()
        tag = ",".join(tag_list)

        print("标题:"+title)
        print("日期:"+create_date)
        print("点赞数:",praise_nums)
        print("收藏数:", fav_nums)
        print("评论数:", comment_nums)
        print("正文:"+content)
        print("标签:"+tag)
        pass

