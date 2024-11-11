# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:49:44 2024

@author: ASUS
"""

#Cho một đoạn văn là một chuỗi ký tự, viết chương trình tìm ra các từ có tỷ lệ xuất hiện lớn hơn 20% trong đoạn văn

from typing import List
def question_31(paragraph: str, n: int) -> List[str]:
    tu = paragraph.lower().split()
    dem_tu = {}
    for i in tu:
        if i in dem_tu:
            dem_tu[i] += 1
        else:
            dem_tu[i] = 1
    lst = []
    for word, count in dem_tu.items():
        if count / len(tu) > 0.2:
           lst.append(word)
    return lst[:n]
if __name__ == '__main__':
    paragraph = "apple apple banana orange orange apple"
    n = 2
    print(question_31(paragraph, n))
    
    paragraph = "hello world hello universe hello"
    n = 1
    print(question_31(paragraph, n))
    