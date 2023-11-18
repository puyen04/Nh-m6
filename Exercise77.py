'''
Viết chương trình chuyển số nhị phân (cơ số 2) thành số thập phân (cơ số 10). 
Chương trình của bạn sẽ bắt đầu bằng cách đọc số nhị phân từ người dùng dưới dạng chuỗi. 
Sau đó, nó sẽ tính số thập phân tương đương bằng cách xử lý từng chữ số trong số nhị phân. 
Cuối cùng, chương trình của bạn sẽ hiển thị số thập phân tương đương với thông báo thích hợp.
'''


binary_number = input('Binary number: ')

decimal_number = 0

for i in range(len(binary_number)):
    digit = int(binary_number[i])

    decimal_number = decimal_number * 2 + digit

print('Equivalent decimal number:', decimal_number)