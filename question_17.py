# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:02:47 2024

@author: ASUS
"""

#Viết một hàm để tạo ra một danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, sắp xếp danh sách theo thứ tự giảm dần.

import random
def question_17(n: int) -> list:
    num = []
    for i in range(n):
        num.append(random.randint(1,100))
    return sorted(num, reverse = True)
if __name__ == '__main__':
    print(question_17(5))
    print(question_17(3))
    