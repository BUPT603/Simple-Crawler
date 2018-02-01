# -*- coding: utf-8 -*-
import scrapy
from weixin.items import WeixinItem

class WeixinspiderSpider(scrapy.Spider):
    name = 'WeixinSpider'
    #allowed_domains = ['weixin']
    start_urls = ['http://weixin.sogou.com/weixin?type=2&query=CYMCO_culture']

    def parse(self, response):
        #print(response.body)#打印出整个回应的body（练习用）
        item = WeixinItem()
        node_list=response.xpath("//div[@class='txt-box']")
        for node in node_list:
            data = node.xpath("./h3/a")#爬取的文字中若带有标签，则需要跳过标签，只取文字
            name = data[0].xpath('string(.)').extract()[0]
            item["name"] = name
            href = node.xpath("./h3/a/@href").extract()[0]
            item["url"] = href
            yield item
            #print (name)
            #print (",")
            #print (href)
        #if len(response.xpath("//div[@class='p-fy']/a[@id='sogou_next']")) != 0:
        #    url = "http://weixin.sogou.com/weixin" + response.xpath("//div[@class='p-fy']/a[@id='sogou_next']/@href").extract()[0]
        #   yield scrapy.Request(url, callback = self.parse)
    
        #pass
