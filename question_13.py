# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:24:08 2024

@author: ASUS
"""

#Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự không phải khoảng trắng.

def question_13(s: str) -> int:
    return len(chuoi.split())
if __name__ == '__main__':
    chuoi = "Hello world, how are you?"
    print(question_13(chuoi))
    
    chuoi = "   This is a test.   "
    print(question_13(chuoi))
