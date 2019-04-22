# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class XiechengPipeline(object):
    # def __init__(self):
    #     # 链接到mysql数据库
    #     self.connect = pymysql.connect(host='114.116.130.123', user='root', password='bigData&G3best!', db='xiecheng', port=3306)
    #     self.cursor = self.connect.cursor() #创建游标用来操作表
    def process_item(self, item, spider):
        with open("city.txt", "a")as fp:
            fp.write(item['cityName'] + item['cityID']+'\n')
        with open("view.txt", "a")as fp:
            fp.write(item['viewNum']+'\n')
            fp.close()
        # 往数据库里面写入数据
    #     self.cursor.execute('insert into city(cityID,cityName,viewNum)VALUES ("{}","{}")'.format(item['cityID'], item['cityName'], item['viewNum']))
    #     self.cursor.execute('insert into view(viewID,'
    #                         'viewName,'
    #                         'peoplegoneNum,'
    #                         'peoplewantNum,'
    #                         'peoplewantNum)VALUES ("{ }","{ }")'.format(item['viewID'],
    #                                                                    item['viewName'],
    #                                                                    item['peoplegoneNum'],
    #                                                                    item['peoplewantNum']))
    #     self.connect.commit()
    #     return item
    # # 关闭数据库
    # def close_spider(self,spider):
    #     self.cursor.close()
    #     self.connect.close()
