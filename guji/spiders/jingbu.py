import scrapy
from scrapy.utils import response

from guji.gujiItem import GujiItem


class Jingbu(scrapy.Spider):
    name = 'jingbu'
    allowed_domains = ['newdu.com']
    start_urls = ['http://ab.newdu.com/book/list-1-1.html']
    newdu_url = 'http://ab.newdu.com'

    # 经部 列表
    def parse(self, response):
        post_type_one = response.xpath('//*[@id="book_right"]/div[2]/div[1]/ul/li/text()').extract()[0]
        bookItem = GujiItem()
        bookItem['post_type_one'] = post_type_one

        for book_url in response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/@href').extract():
            yield scrapy.Request(self.newdu_url+book_url, callback=self.parse_catalog_url,meta={'bookItem': bookItem})

        #经部 列表 分页
        next_url = response.xpath('//*[@id="dedePageList"]/dd[*]/a/@href').extract()
        if next_url:
            yield scrapy.Request(self.newdu_url+next_url[0],callback=self.parse)

    #book 标题 作者 类型 简介 目录章节
    def parse_catalog_url(self,response):
        # book_catalog_title = response.xpath('//*[@id="chapterlist"]/dd[1]/a/text()').extract()
        bookItem = response.meta['bookItem']
        bookItem['post_title'] = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h1/text()').extract()[0]
        bookItem['post_author'] = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[1]/text()').extract()[0]
        bookItem['post_type_two'] = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[2]/a/text()').extract()[0]

        book_catalog_url = response.xpath('//*[@id="chapterlist"]/dd/a/@href').extract()
        for catalog_url in book_catalog_url:
            yield scrapy.Request(self.newdu_url+catalog_url,callback=self.parse_content,meta={'bookItem': bookItem})

    #章节内容
    def parse_content(self,response):
        post_content = response.xpath('//*[@id="book_middle"]/div[1]/div[2]/dl/dd').extract()[0]
        print("=========:"+post_content)
        bookItem = response.meta['bookItem']
        bookItem['post_content'] = post_content
        yield bookItem