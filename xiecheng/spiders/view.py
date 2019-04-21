# -*- coding: utf-8 -*-
import scrapy
import re   # 用于在一串字符中提取数字部分
from xiecheng.items import XiechengItem
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.spiders import Spider


class ViewSpider(scrapy.Spider):
    name = 'view'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://you.ctrip.com/place/']

    # 主站链接 用于拼接
    baseurl = "https://you.ctrip.com"

    # 一级页面解析城市信息以及返回二级页面所需链接

    def parse(self, response):
        cityNames = response.xpath('//div[@id="journals-panel-items"]/dl[2]/dd[@class="panel-con"]/ul/li/a')
        for each_cityNames in cityNames:
            item = XiechengItem()
            item['cityID'] = ','.join(each_cityNames.xpath('@href').re('\d+'))  # re.sub用来提取字符串中的数字部分
            item['cityName'] = each_cityNames.xpath('./text()').extract()[0]
            item['cityUrl'] = ','.join(each_cityNames.xpath('@href').extract()).replace("place", "sight")  # '.'join()将数组转换成字符串,.replace()用来替换字符串
            # 每个城市的链接
            url = self.baseurl + item['cityUrl']
            yield item
            yield scrapy.Request(url, callback=self.getcityInfo)

    # 二级页面解析景点数目以及返回后续页面所需链接

    def getcityInfo(self, response):
        viewNums = response.xpath('//div[@class="ttd_pager cf"]/p')
        views = response.xpath('//div[@class="list_wide_mod2"]')
        item = XiechengItem()
        item['viewNum'] = ','.join(viewNums.xpath('./text()').extract())
        for each_views in views:
            item['viewUrl'] = views.xpath('./dl/dt/a/@href')
            #每个景点的链接
            url = self.baseurl + item['viewUrl']
            yield item
            yield scrapy.Request(url, callback=self.getviewInfo())
        yield item

    # 三级页面解析景点具体数据及总体评论数据

    def getviewInfo(self,response):
        item = XiechengItem()
        viewTitles = response.xpath('//div[@class="cf"]')
        #景点标题部分内容
        for each_viewTitles in viewTitles:
            item['viewID'] = each_viewTitles.xpath('./div[@class="f_left"]/h1/a/@href').re('\d+')
            item['viewName'] = each_viewTitles.xpath('./div[@class="f_left"]/h1/a/text()').extract()[0]
            item['peoplegoneNum'] = each_viewTitles.xpath('./div[@class="f_right"]/li[1]/span[2]/em/text()').extract()
            item['peoplewantNum'] = each_viewTitles.xpath('./div[@class="f_right"]/li[2]/span[2]/em/text()').extract()
        viewInfos = response.xpath('//div[@class="s_sight_infor"]')
        #景点详细信息
        for each_viewInfos in viewInfos:
            item['viewArea'] = each_viewInfos.xpath('./p[@class="s_sight_addr"]/text()').extract()
            item['viewGrade'] = each_viewInfos.xpath('./ul[@class="s_sight_in_list"]/li[1]/span[2]/text()').extract()
            item['viewPhone'] = each_viewInfos.xpath('./ul[@class="s_sight_in_list"]/li[2]/span[2]/text()').extract()
            item['openTime'] = each_viewInfos.xpath('./dl[@class="s_sight_in_list"]/dd/text()').extract()
        commentsAllInfos = response.xpath('//div[@class="comment_wrap"]')
        # 评分及评论
        for each_commentsAllInfos in commentsAllInfos:
            item['scoreScenery'] = each_commentsAllInfos.xpath('./dd[1]/span[@class="score"]/text()').extract()
            item['scoreInterest'] = each_commentsAllInfos.xpath('./dd[2]/span[@class="score"]/text()').extract()
            item['scoreWorth'] = each_commentsAllInfos.xpath('./dd[3]/span[@class="score"]/text()').extract()
            item['CommentNum1'] = each_commentsAllInfos.xpath('./ul[@class="cate_count"]/li[@data-id="3"]/a/span[1]/text()').extract()
            item['CommentNum2'] = each_commentsAllInfos.xpath('./ul[@class="cate_count"]/li[@data-id="4"]/a/span[1]/text()').extract()
            item['CommentNum3'] = each_commentsAllInfos.xpath('./ul[@class="cate_count"]/li[@data-id="2"]/a/span[1]/text()').extract()
            item['CommentNum4'] = each_commentsAllInfos.xpath('./ul[@class="cate_count"]/li[@data-id="1"]/a/span[1]/text()').extract()
            item['CommentNum5'] = each_commentsAllInfos.xpath('./ul[@class="cate_count"]/li[@data-id="5"]/a/span[1]/text()').extract()
            item['CommentNumPerfect'] = each_commentsAllInfos.xpath('./ul[@class="tablist"]/li[2]/a/span/text()').extract()
            item['CommentNumGood'] = each_commentsAllInfos.xpath('./ul[@class="tablist"]/li[3]/a/span/text()').extract()
            item['CommentNumJs'] = each_commentsAllInfos.xpath('./ul[@class="tablist"]/li[4]/a/span/text()').extract()
            item['CommentNumBad'] = each_commentsAllInfos.xpath('./ul[@class="tablist"]/li[5]/a/span/text()').extract()
            item['CommentNumVeryBad'] = each_commentsAllInfos.xpath('./ul[@class="tablist"]/li[6]/a/span/text()').extract()
        #景点简介及交通

        yield item






