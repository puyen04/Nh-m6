# 63, 66, 69, 72, 75, 76, 78
# °F = °C × 9/5 + 32
'''
Viết chương trình hiển thị bảng chuyển đổi nhiệt độ theo độ C và độ F. 
Bảng nên bao gồm các hàng cho tất cả nhiệt độ trong khoảng từ 0 và 100
độ C là bội số của 10 độ C. Bao gồm thích hợp tiêu đề trên các cột của
bạn. Công thức chuyển đổi giữa độ C vàđộ F có thể được tìm thấy trên internet.
'''
print('Celsius ','\t','Fahrenheit')
for C in range(0,101,10):
    F=(C*9/5)+32
    print(C,'\t',F)
