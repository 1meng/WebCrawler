# -*- coding: utf-8 -*-
'''
	如果在parse函数中转码，如item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")，
	而不在管道文件中转码，会抛出如下异常：
	TypeError: Object of type 'bytes' is not JSON serializable
'''
import scrapy
# 导入Tencent工程下面的模块
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']

    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0

    start_urls = [base_url + str(offset)]

    def parse(self, response):
        
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:

        	item = TencentItem()
        	# 提取每个职位的信息，并把它存入item中
        	item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0]
        	item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0]
        	# 处理positionTyp为空的情况
        	if len(node.xpath("./td[2]/text()")):
        		item['positionType'] = node.xpath("./td[2]/text()").extract()[0]
        	else:
        		item['positionType'] = 'None'
        	item['recruitment'] = node.xpath("./td[3]/text()").extract()[0]
        	item['workLocation'] = node.xpath("./td[4]/text()").extract()[0]
        	item['publishTime'] = node.xpath("./td[5]/text()").extract()[0]

        	yield item
			
		# 手动拼接下一页的链接
        # if self.offset < 2850:
        # 	self.offset += 10
        # 	url = self.base_url + str(self.offset)
        # 	yield scrapy.Request(url,callback = self.parse)
		
		# 通过页面中的下一页来获取链接
        if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:

        	url = response.xpath("//a[@id='next']/@href").extract()[0]
        	yield scrapy.Request("http://hr.tencent.com/" + url,callback = self.parse)