import datetime
import urllib.parse

import pypinyin

from guji.utils.mysql import MySQL


class Test:
    def __init__(self):
        self.mysql = MySQL()

    def hp(self,word):
        s = ''
        for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
            s += ''.join(i)
        return s

    def get_term_id(self):
        term_id = 0
        get_term_id_sql = "select a.term_id from wp_terms a where a.name = '{name}'".format(name='易类飞飞')
        print(get_term_id_sql)
        term_id_tup = self.mysql.get_one(get_term_id_sql)
        if term_id_tup:
            term_id = term_id_tup[0]
            print(term_id)
        else:
            wp_terms_data = {'name':'易类飞飞','slug':self.hp('易类飞飞'),'term_group':0}
            self.mysql.insert('wp_terms',wp_terms_data)

    def get_one(self):
        sql = "select a.* from wp_terms a where a.name = '集部'"
        cate_one_id = self.mysql.get_one(sql)[0]
        print(cate_one_id)

    def get_basecode(self):

        values={}
        values['username']='威鹄网'
        values['password']='lushanwenku.com'
        url="http://www.baidu.com"
        data=urllib.parse.urlencode(values)
        print(data)
        s='白话尚书 大战于甘，乃召六卿'
        print(urllib.parse.quote(s))

    def get_html(self):
        from lxml import etree
        import requests
        res=requests.get('http://ab.newdu.com/book/s257777.html')
        tree=etree.HTML(res.content)
        div=tree.xpath('//div[@id="d1"]')[0]
        div_str=etree.tostring(div,encoding='utf-8')
        print (div_str)

if __name__ == '__main__':

    # GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
    # print(datetime.datetime.utcnow().strftime(GMT_FORMAT))
    test = Test()
    #test.get_term_id()
    #print(test.hp("中国"))

    #test.get_one()
    #test.get_html()

    s='白话尚书 大战于甘，乃召六卿'
    encodestr = urllib.parse.quote(s)
    print(encodestr)
    encodestr = '%E8%AE%BA%E8%AF%AD%E6%B3%A8%E9%87%8A_%E7%AB%8B%E8%BA%AB%E5%A4%84%E4%B8%96%E7%9A%84%E4%B8%89%E4%B8%AA%E6%94%AF%E7%82%B9'
    uncodestr = urllib.parse.unquote(encodestr)
    print(uncodestr)