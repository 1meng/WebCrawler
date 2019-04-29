# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class S12306Pipeline(object):

	def __init__(self):

		self.connect = pymysql.connect('localhost','root','107792','12306',charset='utf8')
		self.cursor = self.connect.cursor()

	def process_item(self, item, spider):

		insert_mysql = """insert into timetable(train_code,arrive_time,start_time,station_name,station_no,depart_date) VALUES(%s,%s,%s,%s,%s,%s)
		"""
		self.cursor.execute(insert_mysql,(item['train_code'],item['arrive_time'],item['start_time'],item['station_name'],item['station_no'],item['depart_date']))
		self.connect.commit()

	def close_spider(self,spider):

		self.cursor.close()
		self.connect.close()

class S12306JsonPipeline(object):

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