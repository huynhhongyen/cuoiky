# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:59:09 2024

@author: ASUS
"""

#Cho một danh sách nums chứa các số nguyên. Viết một hàm để tìm phần tử lớn thứ 2 và phần tử nhỏ thứ 5 trong danh sách.

def question_33(nums: list[int]) -> tuple[int, int]:
    nums = sorted(nums)
    if len(nums) < 5:
        return None
    return nums[-2], nums[4]
if __name__ == '__main__':
    nums = [3, 1, 4, 5, 9, 2, 6, 8, 7]
    print(question_33(nums))
    
    nums = [1, 3, 2, 5]
    print(question_33(nums))
    