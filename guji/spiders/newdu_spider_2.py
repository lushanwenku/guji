import scrapy

class NewduSpider(scrapy.Spider):
    name = 'newdu_bak'
    allowed_domains = ['newdu.com']
    start_urls = ['http://ab.newdu.com/book/']
    newdu_url = 'http://ab.newdu.com/book'

    # 经部：
    # 史部：
    # 子部：
    # 集部：
    # 道藏：
    # 佛藏：
    # 小说：
    def parse(self, response):
        cate_nam_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div[*]/dl/dt/a/text()').extract()
        cate_url_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div[*]/dl/dt/a/@href').extract()
        print(cate_nam_list)
        print(cate_url_list)
        for samll_cate_url in cate_url_list:
            print(self.newdu_url+samll_cate_url)
            yield scrapy.Request(self.newdu_url+samll_cate_url,callback=self.parse_next)
        pass

    # 经部：
        # 易类
        # 小学类
        # 乐类
        # 四书类
        # 五经总义类
        # 孝经类
        # 春秋类
        # 礼类
        # 诗类
        # 书类
        # 启蒙蒙学
    def parse_next(self,response):
        small_cate_name_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[1]/text()').extract()
        small_cate_name_url_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[1]/@href').extract()
        book_name_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/text()').extract()
        book_name_url_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/@href').extract()
        book_author_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h2').extract()
        print(small_cate_name_url_list)
        print(book_name_url_list)
        item = GujiItem()
        yield item



    def parse_next(self,response):
        small_cate_name_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[1]/text()').extract()
        small_cate_name_url_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[1]/@href').extract()
        book_name_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/text()').extract()
        book_name_url_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/@href').extract()
        book_author_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h2').extract()
        print(small_cate_name_url_list)
        print(book_name_url_list)
        item = GujiItem()
        yield item