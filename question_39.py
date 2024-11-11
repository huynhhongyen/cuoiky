# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:15:05 2024

@author: ASUS
"""

#Cho một dãy số nằm trong danh sách, đại diện cho giá của một mặt hàng thay đổi qua từng
#ngày. Viết một hàm để tìm ra lợi nhuận lớn nhất có thể đạt được bằng cách thực hiện một
#lần mua và một lần bán, với điều kiện là phải mua mới được bán.

def question_39(prices: list[int]) -> int:
    if not prices:
        return 0
    gia_mua_thap = prices[0]
    loi_nhuan_toi_da = 0
    for gia in prices:
        p = gia - gia_mua_thap
        loi_nhuan_toi_da = max(loi_nhuan_toi_da, p)
        gia_mua_thap = min(gia_mua_thap, gia)
    return loi_nhuan_toi_da
if __name__ == '__main__':
    prices = [6, 7, 8, 9, 20, 5]
    print(question_39(prices))
    
    prices = [7, 1, 5, 3, 6, 4]
    print(question_39(prices))
    
    prices = [7, 6, 4, 3, 1]
    print(question_39(prices))
    