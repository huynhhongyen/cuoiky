# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:13:00 2024

@author: ASUS
"""

#Giả sử bạn đang đứng trước cầu thang có n bậc thang. Mỗi lần bạn có thể bước lên 1 bậc
#hoặc 2 bậc. Viết một hàm để tính số cách bạn có thể leo hết bậc thang.

def question_38(n: int) -> int:
    if n <= 1:
        return 1
    a, b = 1, 1
    for i in range(2,n + 1):
        c = a + b
        a, b = b, c
    return b
if __name__ == '__main__':
    print(question_38(2))
    print(question_38(3))
    