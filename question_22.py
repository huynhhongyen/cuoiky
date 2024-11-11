# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:54:58 2024

@author: ASUS
"""

#Viết một hàm nhận vào một mảng các số nguyên nums. Di chuyển tất cả các số 0 
#trong mảng về cuối mảng trong khi vẫn giữ nguyên thứ tự của các phần tử không phải số 0.

def question_22(nums: list[int]) -> None:
    position = 0
    for i in nums:
        if i != 0:
            nums[position] = i
            position += 1
    for i in range(position, len(nums)):
        nums[i] = 0
    return None
if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    question_22(nums)
    print(nums)
    
    nums = [0, 0, 1]
    question_22(nums)
    print(nums)
    
    nums = [8, 9, 3, 1]
    question_22(nums)
    print(nums)
    