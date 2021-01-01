
class NumToCharUtil():

    _MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
    _P0 = (u'', u'十', u'百', u'千',)
    _S4 = 10 ** 4
    def _to_chinese4(self,num):
        assert (0 <= num and num < self._S4)
        if num < 20:
            return self._MAPPING[num]
        else:
            lst = []
            while num >= 10:
                lst.append(num % 10)
                num = num / 10
            lst.append(num)
            c = len(lst)  # 位数
            result = u''

            for idx, val in enumerate(lst):
                val = int(val)
                if val != 0:
                    result += self._P0[idx] + self._MAPPING[val]
                    if idx < c - 1 and lst[idx + 1] == 0:
                        result += u'零'
            return result[::-1]

    def num_to_char(self,num):
        """数字转中文"""
        num=str(num)
        new_str=""
        num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九"}
        listnum=list(num)
        # print(listnum)
        shu=[]
        for i in listnum:
            # print(num_dict[i])
            shu.append(num_dict[i])
        new_str="".join(shu)
        # print(new_str)
        return new_str

if __name__ == '__main__':
    t = NumToCharUtil()
    print(t._to_chinese4(210))


