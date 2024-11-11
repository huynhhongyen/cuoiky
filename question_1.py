# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:54:21 2024

@author: ASUS
"""

#Bạn được cung cấp một số nguyên dương n. Viết một hàm để xác định xem n có phải là số nguyên tố hay không.

def question_1(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print('n = 2:',question_1(2))
    print('n = 20:',question_1(20))
    print('n = 5:',question_1(5))
