# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:10:21 2024

@author: ASUS
"""

#Cho một chuỗi s chỉ chứa các ký tự '(', ')', '{', '}', '[' và ']'. 
#Viết một hàm để xác định xem chuỗi đầu vào có hợp lệ hay không.

def question_37(s: str) -> bool:
    stack = []
    dct = {'(': ')', '{': '}', '[': ']'}
    for ki_tu in s:
        if ki_tu in dct:
            stack.append(ki_tu)
        else:
            if not stack or dct[stack.pop()] != ki_tu:
                return False
    return not stack
if __name__ == '__main__':
    s = "()"
    print(question_37(s))
    
    s = "()[]{}"
    print(question_37(s))
    
    s = "(]"
    print(question_37(s))
    
    s = "([)]"
    print(question_37(s))
    
    s = "{[]}"
    print(question_37(s))
    