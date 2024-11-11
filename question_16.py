# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:55:03 2024

@author: ASUS
"""

#Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị trung bình cộng của chúng.

def question_16(arg) -> float:
    if not arg:
        return None
    return sum(arg)/len(arg)
if __name__ == '__main__':
    print(question_16([1,2,3,4,5]))
    print(question_16([10,20]))
    print(question_16([]))
    