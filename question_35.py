# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:02:18 2024

@author: ASUS
"""

#Cho một chuỗi đầu vào, tìm chuỗi con lặp lại dài nhất trong chuỗi. 
#Chuỗi con lặp lại là một chuỗi xuất hiện ít nhất hai lần và không được chồng chéo nhau

def question_35(s: str) -> str:
    left, right = 1, len(s) // 2
    do_dai = ""
    while left <= right:
        mid = (left + right) // 2
        chuoi = set()
        for i in range(len(s) - mid + 1):
            chuoi_con = s[i:i + mid]
            if chuoi_con in chuoi:
                do_dai = chuoi_con
                break
            chuoi.add(chuoi_con)
        if do_dai:
            left = mid + 1
        else:
            right = mid - 1
    return do_dai
if __name__ == '__main__':
    s = "aabcdeaabcd"
    print(question_35(s))
    