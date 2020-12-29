import scrapy
import datetime
import urllib.parse

from guji.gujiItem import GujiItem

class NewduSpider(scrapy.Spider):



    # one
    # 经部：
    # 史部：
    # 子部：
    # 集部：
    # 道藏：
    # 佛藏：
    # 小说：
    def parse(self, response):
        cate_one_nam_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div[*]/dl/dt/a/text()').extract()
        cate_one_url_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div[*]/dl/dt/a/@href').extract()
        cate_one_dict = dict(zip(cate_one_nam_list,cate_one_url_list))
        print(cate_one_dict)
        for (k,v) in cate_one_dict.items():
            bookItem = GujiItem()
            bookItem['cate_one_name'] = k.replace("：", "")
            yield scrapy.Request(self.newdu_url+v,callback=self.parse_next_cate_two,meta={'bookItem': bookItem})


        for cate_one_url in cate_one_url_list:
            #print(self.newdu_url+cate_one_url)
            yield scrapy.Request(self.newdu_url+cate_one_url,callback=self.parse_next_cate_two)
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
    def parse_next_cate_two(self,response):
        cate_two_name_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div/dl/dd[*]/a/text()').extract()
        cate_two_url_list = response.xpath('//*[@id="book_right"]/div[1]/div[2]/div/dl/dd[*]/a/@href').extract()
        bookItem = response.meta['bookItem']
        if bookItem['cate_one_name'].strip()=='':
            bookItem['cate_one_name'] = response.xpath('//*[@id="book_right"]/div[2]/div[1]/ul/li/text()').extract()[0]

        for cate_two_url in cate_two_url_list:
            #print(self.newdu_url+cate_two_url)
            yield scrapy.Request(self.newdu_url+cate_two_url,callback=self.parse_next_cate_three_book_list,meta={'bookItem': bookItem})
        pass

    # 易类
        # book_1
        # book_2
        # 春秋左传选译
    def parse_next_cate_three_book_list(self,response):
        book_name_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/text()').extract()
        book_url_list = response.xpath('//*[@id="book_right"]/div[2]/div[2]/div[*]/div[2]/h1/a[2]/@href').extract()
        bookItem = response.meta['bookItem']
        for book_url in book_url_list:
            print(self.newdu_url+book_url)
            yield scrapy.Request(self.newdu_url+book_url,callback=self.parse_next_cate_four_book_chapter_list,meta={'bookItem': bookItem})
        pass

        # 下一页
        next_url = response.xpath('//*[@id="dedePageList"]/dd[9]/a/@href').extract()
        if next_url:
            #print(self.newdu_url+next_url)
            yield scrapy.Request(self.newdu_url+next_url[0],callback=self.parse_next_cate_three_book_list)


    # 春秋左传选译
        # 目录1_《春秋左传》简介
        # 目录2
        # 目录3
    def parse_next_cate_four_book_chapter_list(self,response):
        post_title = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h1/text()').extract()[0]
        post_author_name = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[1]/text()').extract()[0]
        post_term = response.xpath('//*[@id="book_right"]/div/div[1]/div[1]/div[2]/div/h2[2]/a/text()').extract()[0]
        post_description = response.xpath('//*[@id="book_right"]/div/div[1]/div[3]/text()').extract()[0]

        book_chapter_name_list = response.xpath('//*[@id="chapterlist"]/dd[*]/a/text()').extract()
        book_chapter_url_list = response.xpath('//*[@id="chapterlist"]/dd[*]/a/@href').extract()

        bookItem = response.meta['bookItem']
        bookItem['post_title'] = urllib.parse.quote(post_title)
        bookItem['post_author_name'] = post_author_name
        bookItem['post_term'] = post_term
        bookItem['post_description'] = post_description

        for book_chapter_url in book_chapter_url_list:
            #print(self.newdu_url+book_chapter_url)
            yield scrapy.Request(self.newdu_url+book_chapter_url,callback=self.parse_post_content,meta={'bookItem': bookItem})
        pass


    # 《春秋左传》简介
        # 正文
    def parse_post_content(self,response):
        GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
        nowTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)

        book_chapter_name = response.xpath('//*[@id="book_middle"]/div[1]/div[2]/dl/dt/text()').extract()[0]
        post_content_list = response.xpath('//*[@id="book_middle"]/div[1]/div[2]/dl/dd[*]/text()').extract()
        post_content = "".join(post_content_list)
        print(book_chapter_name)
        print(post_content)

        bookItem = response.meta['bookItem']
        #bookItem['ID'] = ID
        bookItem['post_author'] = 6
        bookItem['post_date'] = nowTime
        bookItem['post_date_gmt'] = nowTime
        bookItem['post_content'] = post_content
        #bookItem['post_title'] = post_title
        bookItem['post_excerpt'] = ''
        bookItem['post_status'] = 'publish'
        bookItem['comment_status'] = 'open'
        bookItem['ping_status'] = 'open'
        bookItem['post_password'] = ''
        bookItem['post_name'] = bookItem['post_title']
        bookItem['to_ping'] = ''
        bookItem['pinged'] = ''
        bookItem['post_modified'] = nowTime
        bookItem['post_modified_gmt'] = nowTime
        bookItem['post_content_filtered'] = ''
        bookItem['post_parent'] = 0
        bookItem['guid'] = ''
        bookItem['menu_order'] = 0
        bookItem['post_type'] = 'post'
        bookItem['post_mime_type'] = ''
        bookItem['comment_count'] = 0
        # 非数据库字段
        #bookItem['post_term'] = post_term
        bookItem['book_chapter_name'] = book_chapter_name
        bookItem['post_content'] = post_content
        #bookItem['post_author_name'] = post_author_name

        yield bookItem