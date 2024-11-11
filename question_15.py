# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:49:31 2024

@author: ASUS
"""

#Viết một hàm để kiểm tra xem một biến có giá trị None hay không.

def question_15(value) -> bool:
    if value is None:
        return True
    return False
if __name__ == '__main__':
    value = None
    print(question_15(value))
    
    value = 10
    print(question_15(value))
    
    value = 'Hello'
    print(question_15(value))