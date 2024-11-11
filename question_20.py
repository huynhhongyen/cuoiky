# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:21:23 2024

@author: ASUS
"""

#Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không 
#nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None.

from typing import Optional
def question_20() -> Optional[str]:
    if value == '':
        return None
    return value
if __name__ == '__main__':
    value = input('Nhập giá trị: ')
    print(question_20())
