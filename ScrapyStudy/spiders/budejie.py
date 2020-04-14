# -*- coding: utf-8 -*-
import scrapy
from ScrapyStudy.items import ScrapystudyItem


class BudejieSpider(scrapy.Spider):
    name = "budejie"
    allowed_domains = ["budejie.com"]
    start_urls = ['http://www.budejie.com/text/']
    base_domain="http://www.budejie.com/text/"
    page=1
    def parse(self, response):
        lies=response.xpath('//div[@class="j-r-list"]/ul/li')
        for li in lies:
            username=li.xpath('./div[@class="j-list-user"]/div[@class="u-txt"]/a/text()').get()
            content=li.xpath('.//div[@class="j-r-list-c-desc"]//text()').getall()
            content=" ".join(content).strip()
            item=ScrapystudyItem(username=username,content=content)
            yield item
        next_url=response.xpath('//a[@class="pagenxt"]/@href').get()
        self.page=self.page+1;

        if self.page==5:
            return
        else:
            print("我被调用了%d" % self.page)
            yield scrapy.Request(self.base_domain+str(self.page),callback=self.parse)
