# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class XiechengPipeline(object):
    def __init__(self):
        # 链接到mysql数据库
        print('connecting')
        self.connect = pymysql.connect(
            host='114.116.130.123',
            user='root',
            password='bigData&G3best!',
            db='xiecheng',
            charset='utf8',
            port=3306)
        self.cursor = self.connect.cursor()  # 创建游标用来操作表

    def process_item(self, item, spider):
        try:
            # 往数据库里面写入数据
            self.cursor.execute('insert into view(viewID,viewName,peoplegoneNum,peoplewantNum,'
                                'commentNum,viewArea,viewGrade,viewPhone,openTime,'
                                'scoreScenery,scoreInterest,scoreWorth,'
                                'CommentNum1,CommentNum2,CommentNum3,CommentNum4,CommentNum5,'
                                'CommentNumPerfect,CommentNumGood,CommentNumJs,CommentNumBad,CommentNumVeryBad)VALUES (%s,%s,%s,%s,'
                                '%s,%s,%s,%s,%s,'
                                '%s,%s,%s,'
                                '%s,%s,%s,%s,%s,'
                                '%s,%s,%s,%s,%s,)'.format
                                (item['viewID'], item['viewName'], item['peoplegoneNum'], item['peoplewantNum'],
                                 item['commentNum'], item['viewArea'], item['viewGrade'], item['viewPhone'],
                                 item['openTime'],
                                 item['scoreScenery'], item['scoreInterest'], item['scoreWorth'],
                                 item['CommentNum1'], item['CommentNum2'], item['CommentNum3'], item['CommentNum4'],
                                 item['CommentNum5'],
                                 item['CommentNumPerfect'], item['CommentNumGood'], item['CommentNumJs'],
                                 item['CommentNumBad'], item['CommentNumVeryBad']))
            self.cursor.execute('insert into city(cityID,cityName,viewNum)VALUES (%s,%s,%s)'.format
                                (item['cityID'], item['cityName'], item['viewNum']))
            self.connect.commit()  # 提交
        except Exception as error:
            print('DB is error')
        # 出现错误时打印错误日志


        return item
        # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
