# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:27:16 2024

@author: ASUS
"""

#Viết một hàm tạo ra n số thực ngẫu nhiên trong khoảng từ 0 đến 1. Sau đó, tìm số lớn nhất và số nhỏ nhất trong danh sách đó.

import random
def question_7(n: int) -> (float, float):
    num = []
    for i in range(n):
        num.append(random.uniform(0,1))
    lon_nhat = max(num)
    nho_nhat = min(num)
    return lon_nhat, nho_nhat
if __name__ == '__main__':
    print('Số lớn nhất và số nhỏ nhất trong 5 số thực ngẫu nhiên là',question_7(5))
    