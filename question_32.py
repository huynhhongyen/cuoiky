# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:47:18 2024

@author: ASUS
"""

#Cho một danh sách các số nguyên nums, phân chia danh sách thành hai danh sách:
    #1. Danh sách các số chẵn, được sắp xếp theo thứ tự giảm dần (từ lớn đến nhỏ).
    #2. Danh sách các số lẻ, được sắp xếp theo thứ tự tăng dần (từ nhỏ đến lớn).

from typing import Tuple, List
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    ds_chan = []
    ds_le = []
    for i in nums:
        if i % 2 == 0:
            ds_chan.append(i)
        else:
            ds_le.append(i)
    return sorted(ds_chan, reverse = True), ds_le
if __name__ == '__main__':
    nums = [4, 1, 3, 2, 7, 8, 5]
    print(question_32(nums))
    
    nums = [9, 12, 15, 6, 2, 14]
    print(question_32(nums))
    