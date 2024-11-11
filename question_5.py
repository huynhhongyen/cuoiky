# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:09:33 2024

@author: ASUS
"""

#Viết một hàm để tìm phần tử x trong một danh sách lst. Nếu tìm thấy, trả về vị trí (chỉ số) của phần tử đó, nếu không, trả về None

def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    return None
if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7]
    print(f'lst = {lst}, x = 5 \n{question_5(lst,5)}')
    print(f'lst = {lst}, x = 8 \n{question_5(lst,8)}')
    