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
        numlen = len(self.num) - 1
        denlen = len(self.den) - 1
        strn = ""
        strd = ""
        for i in range(numlen + 1):
            if numlen - i == 0:
                strn += str(self.num[i])
            elif numlen - i == 1:
                strn += str(self.num[i]) + "s + "
            else:
                strn += str(self.num[i]) + "s^" + str(numlen - i) + " + "

        for i in range(denlen + 1):
            if denlen - i == 0:
                strd += str(self.den[i])
            elif denlen - i == 1:
                strd += str(self.den[i]) + "s + "
            else:
                strd += str(self.den[i]) + "s^" + str(denlen - i) + " + "

        return strn + "\n-------\n" + strd

        

    def str_to_tf(tf_str):
        tf_list = re.split(tf_str)
        #case for numerator only
        if '/' in tf_list:
            return
        #case for numerator and denominator