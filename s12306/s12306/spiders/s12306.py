# -*- coding: utf-8 -*-
import json
import scrapy
from s12306.items import S12306Item
from scrapy.http import Request 

class s12306Spider(scrapy.Spider):


	name = 's12306'

	allowed_domains = ['12306.cn/','kyfw.12306.cn']

	start_urls = ['https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-05-01&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=GYW&purpose_codes=ADULT']
	# resp = Request(start_urls[0])

	# print(resp.body)
	def parse(self,response):

		train_list = json.loads(response.body)['data']['result']
		for train in train_list:

			ticket_list = train.split('|')

			if(ticket_list[3].startswith('C') or ticket_list[3].startswith('D') or ticket_list[3].startswith('G')) :

				train_no = ticket_list[2]
				from_station_telecode = ticket_list[4]
				to_station_telecode = ticket_list[7]
				depart_date = ticket_list[13]
				depart_date = depart_date[:4] + '-' + depart_date[4:6] + '-' + depart_date[-2:]

				url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no='

				url = url + train_no + '&from_station_telecode=' + from_station_telecode + '&to_station_telecode=' + to_station_telecode + '&depart_date=' + depart_date
				yield scrapy.Request(url,callback=self.train_info) 

	def train_info(self,response):

		item = S12306Item()

		train_info_list = json.loads(response.body)['data']['data']
		for train_info in train_info_list:

			item['train_code'] = train_info_list[0]['station_train_code']
			item['arrive_time'] = train_info['arrive_time']
			item['start_time'] = train_info['start_time']
			item['station_name'] = train_info['station_name']
			item['station_no'] = train_info['station_no']
			yield item
		# print(train_info_list)