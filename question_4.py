# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:03:47 2024

@author: ASUS
"""

#Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không. 
#Trả về True nếu số đó là số chẵn, và False nếu là số lẻ.

def question_4(n: int) -> bool:
    return n % 2 == 0
if __name__ == '__main__':
    n = int(input('n = '))
    print(question_4(n))
    