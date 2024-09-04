'''
Tạo một chương trình tính giá trị trung bình của một tập hợp các giá trị do người dùng nhập vào.
Người dùng sẽ nhập 0 làm giá trị trọng điểm để cho biết rằng sẽ không cung cấp thêm giá trị nào. 
Chương trình của bạn sẽ hiển thị thông báo lỗi thích hợp nếu giá trị đầu tiên được người dùng nhập là 0.

đã dịch ra tiếng việt
'''

total = 0
count = 0

value = float(input('Value (0 to stop): '))

if value == 0:
    print('Error!!!')
else:
    while value != 0:
        total += value
        count += 1
        value = float(input('Value (0 to stop): '))

    if count == 0:
        print('Error!!!')
    else:
        average = total / count
        print('Average:', average)
