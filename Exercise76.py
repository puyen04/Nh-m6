'''
Bài toán phân tích thành thừa số nguyên tố của một số nguyên n có thể được 
thực hiện bằng các bước sau:

- Khởi tạo biến factor bằng 2.
- Trong khi factor nhỏ hơn hoặc bằng n, thực hiện các bước sau:
- Nếu n chia hết cho factor, kết luận rằng factor là một thừa số của n.
- Chia n cho factor bằng phép chia nguyên.
- Ngược lại, tăng giá trị của factor lên 1.
Viết một chương trình đọc một số nguyên từ người dùng. Nếu giá trị nhập bởi 
người dùng nhỏ hơn 2, chương trình sẽ hiển thị một thông báo lỗi phù hợp. 
Ngược lại, chương trình sẽ hiển thị các số nguyên tố có thể nhân với nhau 
để tính n, với mỗi thừa số xuất hiện trên mỗi dòng. Ví dụ:
'''
n=int(input('Enter an integer: '))
print('Integers are parsed as:')
factor=2
while factor<=n:
    if n%factor==0:
        print(factor)
        n=n//factor
    else:
        factor=factor+1