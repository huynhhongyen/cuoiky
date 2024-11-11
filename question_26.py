# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:20:59 2024

@author: ASUS
"""

#Cho một chuỗi s chỉ gồm các chữ cái viết thường và viết hoa. Viết một hàm để trả 
#về độ dài của chuỗi palindrome dài nhất có thể được tạo ra từ các chữ cái đó. 
#Các chữ cái có phân biệt chữ hoa và chữ thường (ví dụ: "Aa" không được coi là một 
#palindrome). Palindrome là chuỗi đọc giống nhau từ trái sang phải và ngược lại.

def question_26(s: str) -> int:
    dem = {}
    for ky_tu in s:
        if ky_tu in dem:
            dem[ky_tu] += 1
        else:
            dem[ky_tu] = 1
    do_dai = 0
    for i in dem.values():
        if i % 2 == 0:
            do_dai += i
        else:
            do_dai = i - 1
        if i % 2 != 0:
            do_dai += 1
    return do_dai
if __name__ == '__main__':
    s = "abccccdd"
    print(question_26(s))
    
    s = "a"
    print(question_26(s))
    
    s = "bb"
    print(question_26(s))
    