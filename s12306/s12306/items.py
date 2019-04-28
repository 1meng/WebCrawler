# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class S12306Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    train_code = scrapy.Field()

    arrive_time = scrapy.Field()

    start_time = scrapy.Field()

    station_name = scrapy.Field()

    station_no = scrapy.Field()
    
