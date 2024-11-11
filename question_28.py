# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:50:11 2024

@author: ASUS
"""

#Viết một hàm để đếm số lần xuất hiện của từng phần tử (ký tự) trong một chuỗi. Trả về kết
#quả dưới dạng một từ điển, trong đó các khóa là các ký tự và giá trị là số lần xuất hiện 
#của ký tự đó.

from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    dct = {}
    for i in s:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct
if __name__ == '__main__':
    s = "hello"
    print(question_28(s))
    
    s = "test"
    print(question_28(s))
