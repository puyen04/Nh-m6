'''
Chương trình sau đây sử dụng giải thuật để tìm ước số 
chung lớn nhất (GCD) của hai số nguyên dương m và n:

Khởi tạo d với giá trị là số nhỏ nhất giữa m và n.
Trong khi d không chia hết cho cả m và n:
Giảm giá trị của d đi 1.
Báo cáo d là ước số chung lớn nhất của n và m.
Chương trình đọc hai số nguyên dương từ người dùng, sau đó thực hiện giải thuật để xác định và báo cáo ước 
số chung lớn nhất của chúng.
'''
so1 = int(input("Enter the first integer: "))
so2 = int(input("Enter the second integer: "))
UCLN = min(so1, so2)
while so1 % UCLN != 0 or so2 % UCLN != 0:
    UCLN=UCLN-1
print('Greatest common divisor of',so1,'and',so2, 'is:',UCLN)