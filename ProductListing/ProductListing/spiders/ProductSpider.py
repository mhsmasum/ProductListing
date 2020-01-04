import scrapy
from scrapy.selector import Selector
from ProductListing import settings
from ProductListing.items import ProductlistingItem

class ProductSpider(scrapy.Spider):
    name="ProductSpider"
    
    allowed_domains=["www.amazon.com"]
    
    start_urls=['https://www.amazon.com/s?k=deals&i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A7926841011%2Cp_36%3A1253505011&dc&page=1&crid=Y05SHZAOXEPT&qid=1576939850&rnid=386442011&sprefix=Dea%2Caps%2C406&ref=sr_pg_1']

    count = 0 
    
    
    def parse(self,response):
        
        products = response.xpath('//*[@id="search"]/div[1]//div[2]/div/div/div[1]/div/div/div/h2/a[1]/span/text()').extract()
        productUrl = response.xpath('//*[@id="search"]/div[1]//div[2]/div/div/div[1]/div/div/div/h2/a/@href').getall()
        nextPage = response.xpath('//*[@id="search"]/div[1]/div[2]/div/span[8]/div/span/div/div/ul/li[7]/a/@href').get()
       
        if nextPage is not None:
            print('------------------------')
            print(nextPage)
            yield  scrapy.Request( response.urljoin(nextPage) , callback=self.parse )
        
        # for url in  productUrl:
        #     absurl = response.urljoin(url)
        #     yield scrapy.Request( absurl , callback=self.parse_details )
        
        
        
            
            
       


    def parse_details(self , response):
        itemList = list()
        item = ProductlistingItem()
        title = response.css('#productTitle::text').get()
        
        thePrice = None
        price = response.css('.price-large::text').get()
        vendor = response.css('#bylineInfo::text').get()
        priceLarge = response.css('.price-large::text').get()
        pricesmall = response.xpath('//*[@id="usedPitchPrice"]/div[1]/span/span[3]/text()').get()
        
        if title is not None:
            item["ProductName"] = title.strip()
        if vendor is not None:
            item["vendor"]=vendor.strip().replace('by','').strip()
        if priceLarge is not None:
            thePrice = priceLarge.strip()
        if pricesmall is not None:
            thePrice = thePrice+"."+pricesmall.strip()
        if thePrice is not None:
            item["price"]=thePrice
        itemList.append(item)
    
        return itemList
        

        
        

        
        # print(vendor.strip())
        # if price_fetch1 is not None:
        #     print(price_fetch1.strip())
        #     print(price_fetch2.strip())
        # if price_fetch1=='':

        
        #print(productTitle.strip()+"---"+vendor.strip())

        
        
        