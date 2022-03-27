import scrapy
from pro_test.items import ProTestItem

class TestSpider(scrapy.Spider):
    name = 'test'
    # start_urls = ['https://qq.yh31.com/zf/zm/108470.html']
    start_urls = ['https://qq.yh31.com/sx/zw/']
    # 添加持久化数据
    page_num = 2

    def img_detail(self,response):
        img_src = response.xpath('//div[@id="imgBox"]/img/@src').extract_first()
        item = ProTestItem()
        item['src'] = img_src
        yield item

    def parse(self, response):
        img_url_list = response.xpath('//*[@id="main_bblm"]//div[@class="za"]//dt/a/@href').extract()
        for img_url in img_url_list:
            yield scrapy.Request(img_url,callback=self.img_detail)


