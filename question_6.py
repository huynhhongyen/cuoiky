# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:21:30 2024

@author: ASUS
"""

#Viết một hàm để tính giai thừa của số nguyên dương n. Giai thừa của n (ký hiệu là n!) là tích của tất cả các số từ 1 đến n.

def question_6(n: int) -> int:
    giaithua = 1
    for i in range(1,n + 1):
        giaithua *= i
    return giaithua
if __name__ == '__main__':
    print('Giai thừa của 7 là',question_6(7))
    