# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:36:12 2024

@author: ASUS
"""

#Viết một hàm để tìm chuỗi tiền tố chung dài nhất trong một mảng các chuỗi. Nếu không có tiền tố chung, trả về một chuỗi rỗng ""

def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    tien_to = strs[0]
    for i in strs[1:]:
        while i[:len(tien_to)] != tien_to:
            tien_to = tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to
if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(question_27(strs))
    
    strs = ["dog", "racecar", "car"]
    print(question_27(strs))
