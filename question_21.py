# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:31:18 2024

@author: ASUS
"""

#Viết một hàm nhận vào một danh sách số nguyên ngẫu nhiên và một số nguyên dương. 
#Hàm sẽ tìm trong danh sách hai số có tổng bằng với số nguyên dương kia và trả về cặp số đó.

from typing import Optional
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    for i in nums:
        a = target - i
        if a in nums and a != i:
            return i, a
    return None
if __name__ == '__main__':
    print(question_21([2, 7, 11, 15], 9))
    print(question_21([1, 2, 3, 4, 5], 10))
    