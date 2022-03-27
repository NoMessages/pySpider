import scrapy
from scrapy.pipelines.images import ImagesPipeline

class imgPipeLine(ImagesPipeline):

    def get_media_requests(self,item,info):
        yield scrapy.Request(item['src'])

    def file_path(self,request,response=None,info=None):
        imgName = request.url.split('/')[-1]
        return imgName

    def item_completed(self,results,item,info):
        return item