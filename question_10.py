# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:13:06 2024

@author: ASUS
"""

#Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được 
#phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống.

def question_10() -> None:
    ds = input('Nhập các số nguyên (phân cách bằng khoảng trắng): ')
    if not ds:
        return None
    ds = list(map(int, ds.split()))
    return ds
if __name__ == '__main__':
    print(question_10())
    