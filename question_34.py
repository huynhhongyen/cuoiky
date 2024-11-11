# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 20:29:58 2024

@author: ASUS
"""

#Viết một hàm để tìm chuỗi con dài nhất trong chuỗi đầu vào mà không chứa bất kỳ ký tự nào bị lặp lại.

def question_34(s: str) -> int:
    ky_tu = set()
    t = 0
    do_dai = 0
    for p in range(len(s)):
        while s[p] in ky_tu:
            ky_tu.remove(s[t])
            t += 1
        ky_tu.add(s[p])
        do_dai = max(do_dai, p - t + 1)
    return do_dai
if __name__ == '__main__':
    s = "abcabcbb"
    print(question_34(s))
    
    s = "bbbbb"
    print(question_34(s))
    
    s = "pwwkew"
    print(question_34(s))
    