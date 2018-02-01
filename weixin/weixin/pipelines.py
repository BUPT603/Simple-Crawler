# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy import log
from scrapy.conf import settings

class WeixinPipeline(object):
    # def __init__(self):
    #     # 链接数据库
    #     self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
    #     # 数据库登录需要帐号密码的话
    #     # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
    #     self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
    #     self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
    # def process_item(self, item, spider):
    #     postItem = dict(item)  # 把item转化成字典形式
    #     self.coll.insert(postItem)  # 向数据库插入一条记录
    #     return item  # 会在控制台输出原item数据，可以选择不写
    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                #raise DropItem('Missing{0}!'.format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg('question added to mongodb database!',
                    level=log.DEBUG, spider=spider)
        return item


