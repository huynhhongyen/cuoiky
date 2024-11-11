# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:42:27 2024

@author: ASUS
"""

#Viết một hàm nhận vào một mảng số nguyên nums có kích thước n. Trả về phần tử chiếm
#đa số trong mảng. Phần tử chiếm đa số là phần tử xuất hiện nhiều hơn [n / 2] lần. 
#Bạn có thể giả định rằng phần tử chiếm đa số luôn tồn tại trong mảng.

def question_24(nums: list[int]) -> int:
    nums = sorted(nums)
    return nums[len(nums) // 2]
    
if __name__ == '__main__':
    print(question_24([3, 2, 3]))
    print(question_24([2, 2, 1, 1, 1, 2, 2]))
