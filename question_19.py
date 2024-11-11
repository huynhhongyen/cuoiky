# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:12:18 2024

@author: ASUS
"""

#Viết một hàm để kiểm tra xem một số nguyên nhập vào có lớn hơn một số nguyên cho trước n hay không.

def question_19(x: int, n: int) -> bool:
    if x > n:
        return True
    return False
if __name__ == '__main__':
    x = int(input('Nhập một số nguyên: '))
    print(question_19(x,10))
    