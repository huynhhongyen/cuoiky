# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:35:05 2024

@author: ASUS
"""

#Cho một đoạn văn là một chuỗi ký tự, viết chương trình đếm số lượng mỗi từ xuất hiện trong đoạn văn đó.

from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    dct = {}
    key = paragraph.split()
    for i in key:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct
if __name__ == '__main__':
    paragraph = "apple orange apple banana orange"
    print(question_30(paragraph))
    
    paragraph = "hello world hello"
    print(question_30(paragraph))
    