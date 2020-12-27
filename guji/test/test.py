import datetime

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

if __name__ == '__main__':

    # GMT_FORMAT = '%Y-%m-%d %H:%M:%S'
    # print(datetime.datetime.utcnow().strftime(GMT_FORMAT))
    test = Test()
    #test.get_term_id()
    #print(test.hp("中国"))

    test.get_one()