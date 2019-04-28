# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class S12306Pipeline(object):

	def open_spider(self,spider):

		self.f = open("12306.json","wb+")
		self.f.write('['.encode('utf-8'))

	def process_item(self, item, spider):
		content = json.dumps(dict(item),ensure_ascii = False) + ',\n'
		self.f.write(content.encode('utf-8'))
		return item

	def close_spider(self,spider):

		self.f.write('{}]'.encode('utf-8'))
		self.f.close()