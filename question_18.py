# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:10:03 2024

@author: ASUS
"""

#Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:
    #Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
    #Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các từ)
    
def question_18(s: str) -> str:
    return ' '.join(s.split())
if __name__ == '__main__':
    s = "   Hello    world!   "
    print(question_18(s))
    
    s = "Python   is   fun"
    print(question_18(s))
    