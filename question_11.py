# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:41:58 2024

@author: ASUS
"""

#Viết một hàm trả về số Fibonacci thứ n. 

def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        a,b = 0,1
        for i in range(2,n + 1):
            a,b = b, a + b
        return b
if __name__ == '__main__':
    print('Số Fibonacci thứ 5:',question_11(5))
    print('Số Fibonacci thứ 10:',question_11(10))
    print('Số Fibonacci thứ 0:',question_11(0))