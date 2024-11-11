# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:36:44 2024

@author: ASUS
"""

#Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. 
#Chuỗi được coi là chữ số nếu tất cả các ký tự trong chuỗi là số và không có ký tự nào khác.

def question_14(s: str) -> bool:
    if s.isdigit():
        return True
    return False
if __name__ == '__main__':
    print(question_14('12fr345'))
    print(question_14('12345'))
    print(question_14(' '))
