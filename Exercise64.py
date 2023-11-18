'''
4/2/2013 là ngày cuối cùng đồng xu được phân phối bởi Sở đúc tiền Hoàng gia Canada. 
Giờ đây, đồng xu đã bị loại bỏ dần, các nhà bán lẻ phải điều chỉnh tổng số sao cho chúng là bội số của 5 xu khi chúng được thanh toán bằng tiền mặt 
(các giao dịch thẻ tín dụng và thẻ ghi nợ tiếp tục được tính bằng đồng xu). 
Mặc dù các nhà bán lẻ có một số quyền tự do trong cách họ thực hiện việc này nhưng hầu hết đều chọn làm tròn đến đồng niken gần nhất.
Viết chương trình đọc giá từ người dùng cho đến khi nhập vào một dòng trống. 
Hiển thị tổng chi phí đã nhập trên một dòng, theo sau là số tiền phải trả nếu khách hàng thanh toán bằng tiền mặt trên dòng thứ hai. 
Số tiền đến hạn thanh toán bằng tiền mặt phải được làm tròn đến đồng niken gần nhất. 
Một cách để tính số tiền thanh toán bằng tiền mặt là bắt đầu bằng việc xác định cần bao nhiêu xu để thanh toán tổng số tiền. 
Sau đó tính số dư khi chia số xu này cho 5. 
Cuối cùng, điều chỉnh tổng số xuống nếu số dư nhỏ hơn 2,5. 
Còn không thì điều chỉnh tổng lên.
'''

total_cost = 0

while True:
    price_input = input('Price (blank line to finish): ')

    if price_input == "": break

    price = float(price_input)
    total_cost += price

pennies_due = total_cost * 100
remainder = pennies_due % 5

if remainder < 2.5:
    adjusted_total = pennies_due - remainder
else:
    adjusted_total = pennies_due + (5 - remainder)

amount_due_cash = adjusted_total / 100

print('Total cost: ', round(total_cost,2), '$', sep='')
print('Amount due (cash): ', round(amount_due_cash,3), '$', sep='')