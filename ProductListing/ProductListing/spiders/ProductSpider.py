import scrapy
from scrapy.selector import Selector
from ProductListing import settings
from ProductListing.items import ProductlistingItem

class ProductSpider(scrapy.Spider):
    name="ProductSpider"
    allowed_domains=["www.amazon.com"]
    
    #start_urls=['https://www.amazon.com/s?i=automotive-intl-ship&bbn=2562090011&rh=n%3A2562090011%2Cn%3A15690151%2Cn%3A15736321&dc&page=2&fst=as%3Aoff&qid=1576906774&rnid=15690151&ref=sr_pg_1']
    start_urls=['https://www.amazon.com/s?k=deals&i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A7926841011%2Cp_36%3A1253505011&dc&page=1&crid=Y05SHZAOXEPT&qid=1576939850&rnid=386442011&sprefix=Dea%2Caps%2C406&ref=sr_pg_1']


    
    
    def parse(self,response):
        
        products = response.xpath('//*[@id="search"]/div[1]//div[2]/div/div/div[1]/div/div/div/h2/a[1]/span/text()').extract()
        productUrl = response.xpath('//*[@id="search"]/div[1]//div[2]/div/div/div[1]/div/div/div/h2/a/@href').getall()
        
        # productLength = len(productUrl)
        # print(products)
        # print(productLength)
        for url in  productUrl:
            absurl = response.urljoin(url)
            yield scrapy.Request( absurl , callback=self.parse_details )
            
       


    def parse_details(self , response):
        

        atitle = response.xpath("//body[1]/div[2]/div[1]/div[5]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/h1[1]/span[1]/text()").extract()
        atitle = response.xpath('/body/div[1]/div[5]/div[3]/div[3]/div/div[2]/div[1]/div[1]/div/h1/span')
        # atitle = response.xpath('//span[contains(@id, "productTitle")]').extract()
        print ("-------------------")
        print(atitle)

        
        

        
        # print(vendor.strip())
        # if price_fetch1 is not None:
        #     print(price_fetch1.strip())
        #     print(price_fetch2.strip())
        # if price_fetch1=='':

        
        #print(productTitle.strip()+"---"+vendor.strip())

        
        
        