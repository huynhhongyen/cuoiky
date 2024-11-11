# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:06:39 2024

@author: ASUS
"""

#Cho một mảng nums gồm các số nguyên khác nhau. Viết một hàm để trả về tất cả 
#các hoán vị có thể của mảng đó. Bạn có thể trả về kết quả theo bất kỳ thứ tự nào.

def question_36(nums: list[int]) -> list[list[int]]:
    ket_qua = [[]]
    for n in nums:
        ds = []
        for hoan_vi in ket_qua:
            for i in range(len(hoan_vi) + 1):
                hvi = hoan_vi[:i] + [n] + hoan_vi[i:]
                ds.append(hvi)
        ket_qua = ds
    return ket_qua
if __name__ == '__main__':
    nums = [1, 2, 3]
    print(question_36(nums))
    
    nums = [0, 1]
    print(question_36(nums))
    
    nums = [1]
    print(question_36(nums))
    