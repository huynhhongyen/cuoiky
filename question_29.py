# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:00:54 2024

@author: ASUS
"""

#Tìm số trung vị của một danh sách.
    #Số trung vị của một danh sách các số nguyên là giá trị ở vị trí giữa khi danh sách được 
    #sắp xếp theo thứ tự tăng dần. Nếu danh sách có số lượng phần tử là lẻ, số trung vị là 
    #giá trị giữa. Nếu danh sách có số lượng phần tử là chẵn, số trung vị là trung bình cộng 
    #của hai giá trị ở giữa. 

from typing import List
def question_29(nums: List[int]) -> float:
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n//2] + nums[n//2 - 1]) / 2
    return nums[n//2]
if __name__ == '__main__':
    nums = [1, 3, 4, 2, 5]
    print(question_29(nums))
    
    nums = [1, 2, 3, 4]
    print(question_29(nums))
