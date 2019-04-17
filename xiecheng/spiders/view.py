# -*- coding: utf-8 -*-
import scrapy
from xiecheng.items import XiechengItem

class ViewSpider(scrapy.Spider):
    name = 'view'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://you.ctrip.com/place/']
    # 发送当前页的请求和读出后面所有页的网络请求
    def parse(self, response):
        cityNames = response.xpath('//div[@id="journals-panel-items"]/dl[2]/dd[@class="panel-con"]/ul/li/a')

        for each_cityNames in cityNames:
            item = XiechengItem()
            item['cityName'] = each_cityNames.xpath('./text()').extract()[0]
            yield item


    # def parse_page(self, response):
    #     for item in response.xpath():
    #         view = XiechengItem()
    #         # view['cityID'] = item.xpath().extract()[0]
    #         view['cityName'] = item.xpath().extract()[0]
    #         # view['viewNum'] = item.xpath().extract()[0]
    #         # view['viewID'] = item.xpath().extract()[0]
    #         # view['viewName'] = item.xpath().extract()[0]
    #         yield view



