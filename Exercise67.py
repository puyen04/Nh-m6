'''
Một vườn thú cụ thể xác định giá vào cửa dựa trên độ tuổi của khách. 
Khách từ 2 tuổi trở xuống được vào miễn phí. Trẻ em từ 3 đến 12 tuổi có giá 14 USD. 
Người cao niên từ 65 tuổi trở lên có giá $18,00. Vé vào cửa cho tất cả các khách khác là $23,00.
Tạo một chương trình bắt đầu bằng cách đọc độ tuổi của tất cả khách trong nhóm từ người dùng, với một độ tuổi được nhập trên mỗi dòng. 
Người dùng sẽ nhập một dòng trống để thông báo không còn khách trong nhóm. 
Sau đó, chương trình của bạn sẽ hiển thị chi phí nhập học của nhóm với một thông báo thích hợp. 
Chi phí phải được hiển thị bằng hai chữ số thập phân.
'''

total_cost = 0

while True:
    age_input = input('Age of guest (blank line to finish): ')

    if age_input == "": break

    age = int(age_input)
    if age <= 2:
        cost = 0
    elif 3 <= age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00

    total_cost += cost

print('Total admission cost for the group: ', round(total_cost,2),'$', sep='')