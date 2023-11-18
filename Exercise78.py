'''
Viết một chương trình chuyển đổi một số thập phân (hệ cơ số 10) sang số nhị phân (hệ cơ số 2). 
Đọc số thập phân từ người dùng dưới dạng số nguyên, sau đó sử dụng thuật toán chia lấy dư được 
mô tả dưới đây để thực hiện quá trình chuyển đổi. Khi thuật toán hoàn thành, biến "result" 
chứa biểu diễn nhị phân của số. Hiển thị kết quả, kèm theo một thông báo phù hợp.

Đặt "result" là một chuỗi rỗng.
Đặt "q" là số cần chuyển đổi.
Lặp lại:
Đặt "r" bằng phần dư khi "q" được chia cho 2.
Chuyển "r" thành chuỗi và thêm vào đầu "result".
Chia "q" cho 2, bỏ bất kỳ phần dư nào, và lưu kết quả lại vào "q".
Lặp lại bước 3 cho đến khi "q" trở thành 0.
'''
q=int(input('Enter the decimal number: '))
result=''
while q>0:
    du=q%2
    result=str(du) +result
    q=q//2
print('Binary numbers are: ',result)