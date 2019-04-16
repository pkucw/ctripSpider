# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 定义爬虫需要返回的字段
import scrapy



class XiechengItem(scrapy.Item):
    # define the fields for your item here like:

    # 城市表
    # 城市ID
    # cityID = scrapy.Field()
    # 城市名称
    cityName = scrapy.Field()
    # 景点个数
    # viewNum = scrapy.Field()

    # 景点表
    # 景点ID
    # viewID = scrapy.Field()
    # 景点名称
    # viewName = scrapy.Field()
    # 景点评分
    # viewScore = scrapy.Field()
    # # 景点排名
    # viewTop = scrapy.Field()
    # 景点评论条数
    # commentNum = scrapy.Field()
    # 想去人数
    # peopleNum = scrapy.Field()
    # 去过人数
    # peopledNum = scrapy.Field()
    # 景点地址
    # viewArea = scrapy.Field()
    # 等级？？？？
    # 电话？？？？
    # 开放时间
    # openTime = scrapy.Field()
    # 景点简介
    # viewIntro = scrapy.Field()
    # 交通
    # viewTrans = scrapy.Field()
    # 景色得分
    # scoreScenery = scrapy.Field()
    # 趣味得分
    # scoreInterest = scrapy.Field()
    # 性价比得分
    # scoreWorth = scrapy.Field()
    # 评论条数（情侣出游）
    # CommentNum1 = scrapy.Field()
    # 评论条数（家庭亲子）
    # CommentNum2 = scrapy.Field()
    # 评论条数（朋友出游）
    # CommentNum3 = scrapy.Field()
    # 评论条数（商务旅行）
    # CommentNum4 = scrapy.Field()
    # 评论条数（单独旅行）
    # CommentNum5 = scrapy.Field()
    # 评论条数（很好）
    # CommentNumPerfect = scrapy.Field()
    # 评论条数（好）
    # CommentNumGood = scrapy.Field()
    # 评论条数（一般）
    # CommentNumJs = scrapy.Field()
    # 评论条数（差）
    # CommentNumBad = scrapy.Field()
    # 评论条数（很差）
    # CommentNumVeryBad = scrapy.Field()

    # 景点评论表
    # 评论ID
    # CommentID = scrapy.Field()
    # 评论内容
    # CommentContent = scrapy.Field()
    # 景色评分
    # CommentscoreScenery = scrapy.Field()
    # 趣味评分
    # CommentscoreInterest = scrapy.Field()
    # 性价比评分
    # CommentscoreWorth = scrapy.Field()
    # 评论者ID
    # CommentPersonID = scrapy.Field()
    # 评论者昵称
    # CommentNickname = scrapy.Field()
    # 评论综合分数
    # Commentscore = scrapy.Field()
    # 有用数量
    # WorthNum = scrapy.Field()
    # 评论日期
    # CommentTime = scrapy.Field()



