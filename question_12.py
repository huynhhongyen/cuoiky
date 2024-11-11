# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:06:52 2024

@author: ASUS
"""

#Viết một hàm để tạo ra một số nguyên ngẫu nhiên từ 1 đến 1000. Sau đó, kiểm tra xem số đó có phải là số nguyên tố hay không.

import random
def question_12() -> bool:
    n = random.randint(1,1000)
    print(n)
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    print(question_12())