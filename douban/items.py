# -*- coding: utf-8 -*-
import scrapy


class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()            # 书名
    price = scrapy.Field()           # 价格
    edition_year = scrapy.Field()    # 出版年份
    publisher = scrapy.Field()       # 出版社
    ratings = scrapy.Field()         # 评分
    author = scrapy.Field()          # 作者
    content = scrapy.Field()
