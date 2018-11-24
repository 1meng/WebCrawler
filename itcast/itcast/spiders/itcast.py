# -*- coding: utf-8 -*-
import scrapy
from itcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")
        
        # items = []
        for node in node_list:

        	item = ItcastItem()

        	item['name'] = node.xpath("./h3/text()").extract()[0]
        	item['title'] = node.xpath("./h4/text()").extract()[0]
        	item['info'] = node.xpath("./p/text()").extract()[0]

        	# 每个item都会返回，并返回这里继续执行
        	yield item
        	# items.append(item)

        # return items