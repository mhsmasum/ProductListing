# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductlistingItem(scrapy.Item):
    
    ProductName = scrapy.Field()
    vendor = scrapy.Field()
    price =scrapy.Field()

    

    
