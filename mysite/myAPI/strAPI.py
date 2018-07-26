# -*- coding: utf-8 -*-
'''
使用举例：
from myAPI.strAPI import strAPI
if strAPI('in input').isStr('input'): True

Created on 2017-05-29
'''

def getstr():
    return 'hello world!'  

class strAPI:
    def __init__(self, str):
        self.str = str
    
    def isStr(self,MyStr):
        return MyStr in self.str #(strAPI('hello world!').isStr('hello w'),True) 
    
    def isList(self,MyList):
        return self.str in MyList #(strAPI('hellow').isList(['hello','world']),False)    
    
    def getStr1Str2(self,s):#strAPI('helloworld!').getStr1Str2('o'),('hello', 'world!')
        pos = self.str.find(s)+1 #搜索第一个s字符串的位置
        if pos>0:
            return self.str[:pos],self.str[pos:]
        return '',''

import unittest            
class TeststrAPI(unittest.TestCase):
    def test_isStr1(self):
        s=strAPI('hello world!')
        self.assertEquals(s.isStr('hello w'),True)          
    def test_isStr2(self):
        self.assertEquals(strAPI('helloworld!').isStr(''),True) 
    def test_isStr3(self):
        self.assertEquals(strAPI('helloworld!').isStr(' '),False) 
                 

    def test_isList1(self):
        self.assertEquals(strAPI('hello').isList(['hello','world']),True)          
    def test_isList2(self):
        self.assertEquals(strAPI('hellow').isList(['hello','world']),False)          
    def test_isList3(self):
        self.assertEquals(strAPI('hell').isList(['hello','world']),False)          

    def test_getStr1Str2(self):
        self.assertEquals(strAPI('helloworld!').getStr1Str2('o'),('hello', 'world!'))          


if __name__ == '__main__':
    unittest.main()