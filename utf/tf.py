import re

class tf:
    num = []
    den = []

    def __init__(self, n, d=[]):
        self.num = n
        self.den = d

    def pprint(self):
        print(self.tf_to_str())

    def tf_to_str(self):
        if type(self.num) == int and type(self.den) == int:
            return str(self.num) + "\n-------\n" + str(self.den)

        numlen = len(self.num) - 1
        denlen = len(self.den) - 1

        if numlen == -1 or (numlen == 0 and self.num[0] == 0):
            return "0"
        
        if denlen == -1 or (denlen == 0 and self.den[0] == 0):
            raise ZeroDivisionError
        
        strn = ""
        strd = ""
        for i in range(numlen + 1):
            ni = str(self.num[i])
            print(ni)
            if ni == "0":
                if i == numlen:
                    strn = strn[:-3]
                continue
            if numlen - i == 0:
                strn += ni
            elif numlen - i == 1:
                if ni == "1":
                    ni = ""
                strn += ni + "s + "
            else:
                if ni == "1":
                    ni = ""
                strn += ni + "s^" + str(numlen - i) + " + "

        for i in range(denlen + 1):
            di = str(self.den[i])
            if di == "0":
                if i == denlen:
                    strd = strd[:-3]
                continue
            if denlen - i == 0:
                strd += di
            elif denlen - i == 1:
                strd += di + "s + "
            else:
                strd += di + "s^" + str(denlen - i) + " + "

        return strn + "\n-------\n" + strd

        

    def str_to_tf(self, tf_str):
        tf_list = re.split(tf_str)
        #case for numerator only
        if '/' in tf_list:
            return
        #case for numerator and denominator