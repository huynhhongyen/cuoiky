# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:41:27 2024

@author: ASUS
"""

#Viết một hàm để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không. Một chuỗi
#được gọi là palindrome nếu sau khi chuyển tất cả các chữ cái viết hoa thành chữ thường
#và loại bỏ tất cả các ký tự không phải chữ cái và số, nó đọc giống nhau từ trái sang phải 
#và từ phải sang trái.

def question_9(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == str(s)[::-1]
if __name__ == '__main__':
    print(question_9("A man, a plan, a canal: Panama"))
    print(question_9("race a car"))
    