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
            item['cityUrl'] = ','.join(each_cityNames.xpath('@href').extract()).replace("place", "sight")  # '.'join()将数组转换成字符串,.replace()用来替换字符串
            # 每个城市的链接
            print('ok')
            cityurl = self.baseurl+item['cityUrl']
            yield item
            yield scrapy.Request(cityurl, callback=self.getcityInfo)


    # 二级页面解析景点数目以及返回后续页面所需链接

    def getcityInfo(self, response):
        item = XiechengItem()
        cityinfo = response.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/h1/a')
        # 在每个城市景点的第一页获取城市名称、城市ID
        for each_cityinfo in cityinfo:
            item['cityID'] = ','.join(each_cityinfo.xpath('@href').re('\d+')) # re.sub用来提取字符串中的数字部分
            item['cityName'] = each_cityinfo.xpath('@title').extract()[0]
        # 在每个城市景点的第一页获取城市中的景点个数
        viewNums = response.xpath('//div[@class="ttd_pager cf"]/p')
        views = response.xpath('/html/body/div[4]/div/div[2]/div/div[3]/div/div[2]/dl/dt/a')
        item['viewNum'] = viewNums.xpath('./text()').re('\d+')[2]
        yield item

        # 从这里开始注释
        # 获取当前页的每个景点链接
        for each_views in views:
            item['viewUrl'] = ','.join(each_views.xpath('./@href').extract())
            # 每个景点的链接
            viewurl = self.baseurl + item['viewUrl']
            yield scrapy.Request(viewurl, callback=self.getviewInfo)

        # 连续获取下一页的链接
        next_page = response.xpath('//a[@class="nextpage"]/@href').extract_first()  # 获取下一页链接
        if next_page is not None:
            next_page = self.baseurl+next_page
            item = XiechengItem()
            item['nextpage'] = next_page
            yield scrapy.Request(next_page, callback=self.getcityInfo)
        yield item

    # 三级页面解析景点具体数据及总体评论数据

    def getviewInfo(self, response):
        item = XiechengItem()
        # 景点标题部分内容
        item['viewID'] = response.xpath('/html/body/div[2]/div[2]/div/div[1]/h1/a/@href').re('\d+')[1]  # 提取字符串中的第二个数字
        item['viewName'] = response.xpath('/html/body/div[2]/div[2]/div/div[1]/h1/a/text()').extract()[0]
        item['commentNum'] = response.xpath('//*[@id="hrefyyDp"]/span/text()').extract()[0]
        item['peoplegoneNum'] = response.xpath('//*[@id="emWentValueID"]/text()').extract()[0]
        item['peoplewantNum'] = response.xpath('//*[@id="emWantValueID"]/text()').extract()[0]
        # 景点详细信息
        viewInfos = response.xpath('//div[@class="s_sight_infor"]')
        for each_viewInfos in viewInfos:
            item['viewArea'] = each_viewInfos.xpath('./p[@class="s_sight_addr"]/text()').extract()[0]
            item['viewGrade'] = each_viewInfos.xpath('./ul[@class="s_sight_in_list"]/li[1]/span[2]/text()').extract()[0].strip()  # .strip()函数去除/n/r空格等
            item['viewPhone'] = each_viewInfos.xpath('./ul[@class="s_sight_in_list"]/li[2]/span[2]/text()').extract()[0].strip()
            item['openTime'] = each_viewInfos.xpath('./dl[@class="s_sight_in_list"]/dd/text()').extract()[0]
        # 评分及评论
        commentsAllInfos = response.xpath('//*[@id="weiboCom1"]')
        for each_commentsAllInfos in commentsAllInfos:
            item['scoreScenery'] = each_commentsAllInfos.xpath('./div[1]/dl/dd[1]/span[3]/text()').extract()[0]
            item['scoreInterest'] = each_commentsAllInfos.xpath('./div[1]/dl/dd[2]/span[3]/text()').extract()[0]
            item['scoreWorth'] = each_commentsAllInfos.xpath('./div[1]/dl/dd[3]/span[3]/text()').extract()[0]
            item['CommentNum1'] = each_commentsAllInfos.xpath(
                './div[1]/ul/li[1]/a/span[1]/text()').re('\d+')[0]
            item['CommentNum2'] = each_commentsAllInfos.xpath(
                './div[1]/ul/li[2]/a/span[1]/text()').re('\d+')[0]
            item['CommentNum3'] = each_commentsAllInfos.xpath(
                './div[1]/ul/li[3]/a/span[1]/text()').re('\d+')[0]
            item['CommentNum4'] = each_commentsAllInfos.xpath(
                './div[1]/ul/li[4]/a/span[1]/text()').re('\d+')[0]
            item['CommentNum5'] = each_commentsAllInfos.xpath(
                './div[1]/ul/li[5]/a/span[1]/text()').re('\d+')[0]
            item['CommentNumPerfect'] = each_commentsAllInfos.xpath(
                './div[2]/ul/li[2]/a/span/text()').re('\d+')[0]
            item['CommentNumGood'] = each_commentsAllInfos.xpath('./div[2]/ul/li[3]/a/span/text()').re('\d+')[0]
            item['CommentNumJs'] = each_commentsAllInfos.xpath('./div[2]/ul/li[4]/a/span/text()').re('\d+')[0]
            item['CommentNumBad'] = each_commentsAllInfos.xpath('./div[2]/ul/li[5]/a/span/text()').re('\d+')[0]
            item['CommentNumVeryBad'] = each_commentsAllInfos.xpath(
                './div[2]/ul/li[5]/a/span/text()').re('\d+')[0]
        # 景点简介及交通
        item['viewIntro'] = response.xpath('/html/body/div[3]/div/div[1]/div[5]/div[2]/div[1]/div/text()').extract()[
            0].strip()

        yield item






