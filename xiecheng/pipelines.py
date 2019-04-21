# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiechengPipeline(object):
    def process_item(self, item, spider):
        with open("city.txt", "a")as fp:
            fp.write(item['cityName']+item['cityID'] + '\n')
        with open("view.txt", "a")as fp:
            fp.write(item['viewNum']+'\n')
            fp.close()
        return item
