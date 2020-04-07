# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta

class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['https://www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']
    
    def parse(self, response):
        
        for each in response.xpath('//*[@id="main_table_countries_yesterday"]/tbody/tr'):
	        yield {
	            'country': each.xpath('td[1]//text()').extract(),
	            'total_cases': each.xpath('td[2]//text()').extract(),
	            'new_cases': each.xpath('td[3]//text()').extract(),
	            'total_deaths': each.xpath('td[4]//text()').extract(),
	            'new_deaths': each.xpath('td[5]//text()').extract(),
	            'total_recovered': each.xpath('td[6]//text()').extract(),
	            'date' : date.today() - timedelta(days=1)
	        }