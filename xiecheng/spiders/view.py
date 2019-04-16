# -*- coding: utf-8 -*-
import scrapy
from xiecheng.items import XiechengItem

class ViewSpider(scrapy.Spider):
    name = 'view'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://you.ctrip.com/place/']
    # 发送当前页的请求和读出后面所有页的网络请求
    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parse_page)
        for page in response.xpath('//dd[@class="panel-con"]/a'):
            link = page.xpath('@href').extract()[0]
            yield scrapy.Request(link, callback=self.parse_page)

    def parse_page(self, response):
        for item in response.xpath():
            view = XiechengItem()
            # view['cityID'] = item.xpath().extract()[0]
            view['cityName'] = item.xpath().extract()[0]
            # view['viewNum'] = item.xpath().extract()[0]
            # view['viewID'] = item.xpath().extract()[0]
            # view['viewName'] = item.xpath().extract()[0]
            yield view



