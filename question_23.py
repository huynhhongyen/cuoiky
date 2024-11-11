# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:21:22 2024

@author: ASUS
"""

#Viết một hàm nhận vào một mảng các số nguyên nums. Trả về True nếu có bất kỳ giá trị nào 
#xuất hiện ít nhất hai lần trong mảng, và trả về False nếu tất cả các phần tử trong mảng đều khác nhau.

def question_23(nums: list[int]) -> bool:
    ds = set()
    for i in nums:
        if i in ds:
            return True
        ds.add(i)
    return False
if __name__ == '__main__':
    print(question_23([1, 2, 3, 1]))
    print(question_23([1, 2, 3, 4]))
    print(question_23([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(question_23([]))
