# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
	# 职位名称
    positionName = scrapy.Field()

    positionLink = scrapy.Field()

    positionType = scrapy.Field()

    recruitment = scrapy.Field()

    workLocation = scrapy.Field()

    publishTime = scrapy.Field()