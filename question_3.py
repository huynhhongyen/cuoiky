# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:44:16 2024

@author: ASUS
"""

#Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết thường trong chuỗi đó.

def question_3(s: str) -> (int, int):
    chu_hoa = 0
    chu_thuong = 0
    for chu in s:
        if chu.isupper():
            chu_hoa += 1
        if chu.islower():
            chu_thuong += 1
    return chu_hoa, chu_thuong
if __name__ == '__main__':
    print('s = \'Hello World\' \nSố lượng ký tự viết hoa và viết thường là',question_3('Hello World'))
    