# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 16:22:14 2024

@author: ASUS
"""

#Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, tính tổng và trung bình của các số này.

import random
def question_2(n: int) -> (int, float):
    num = []
    for i in range(n):
        num.append(random.randint(1,100))
    tong = sum(num)
    trungbinh = tong/n
    return tong, trungbinh
if __name__ == '__main__':
    print('n = 5 \nTổng và trung bình của 5 số nguyên ngẫu nhiên là',question_2(5))
