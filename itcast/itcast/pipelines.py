# -*- coding: utf-8 -*-

# 使用了管道，就用在setting.py中取消掉ITEM_PIPELINES的注释
import json

class ItcastPipeline(object):
	def open_spider(self,spider):
		self.f = open("itcast_test.json","wb+")
		self.f.write("[".encode("utf-8"))

	def process_item(self, item, spider):

		content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
		self.f.write(content.encode("utf-8"))
		return item

	def close_spider(self,spider):
		# 写入一个空对象
		self.f.write("{}]".encode("utf-8"))
		self.f.close()