# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 21:58:40 2024

@author: ASUS
"""

#Cho một mảng các số nguyên nums đã được sắp xếp theo thứ tự không giảm. Viết một hàm
#để trả về một mảng chứa bình phương của mỗi số trong nums và mảng này cũng phải được 
#sắp xếp theo thứ tự không giảm.

def question_25(nums: list[int]) -> list[int]:
    binhphuong = []
    for i in nums:  
        binhphuong.append(i**2)
    return sorted(binhphuong)
if __name__ == '__main__':
    nums = [-4,-1, 0, 3, 10]
    print(question_25(nums))
    
    nums = [-7,-3, 2, 3, 11]
    print(question_25(nums))
    