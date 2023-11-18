'''
Một trong những ví dụ đầu tiên về mã hóa được biết đến là Julius Caesar. 
Caesar cần cung cấp hướng dẫn bằng văn bản cho các tướng lĩnh của mình, 
nhưng ông không muốn kẻ thù biết được kế hoạch của mình nếu thông điệp lọt vào tay họ. 
Kết quả là ông đã phát minh ra Mật mã Caesar.
Ý tưởng đằng sau mật mã này rất đơn giản (và kết quả là nó không cung cấp sự bảo vệ nào trước các kỹ thuật phá mã hiện đại).
Mỗi chữ cái trong tin nhắn gốc được dịch chuyển 3 vị trí. 
Kết quả là A trở thành D, B trở thành E, C trở thành F, D trở thành G, v.v. 
Ba chữ cái cuối cùng trong bảng chữ cái được quấn quanh phần đầu: X trở thành A, Y trở thành B và Z trở thành C. 
Không phải các ký tự chữ cái không bị sửa đổi bởi mật mã.
Viết chương trình thực hiện mật mã Caesar. 
Cho phép người dùng cung cấp tin nhắn và số lượng ca, sau đó hiển thị thông báo đã dịch chuyển. 
Đảm bảo rằng chương trình của bạn mã hóa cả chữ hoa và chữ thường. 
Chương trình của bạn cũng phải hỗ trợ các giá trị dịch chuyển âm để có thể sử dụng nó để mã hóa tin nhắn và giải mã tin nhắn.
'''

message = input('Message: ')
shift = int(input('The shift amount (positive or negative): '))

encrypted_message = ''

for char in message:
    if char.isalpha():
        is_uppercase = char.isupper()

        shifted_char = chr((ord(char) - ord('A' if is_uppercase else 'a') + shift) % 26 + ord('A' if is_uppercase else 'a'))

        encrypted_message += shifted_char
    else:
        encrypted_message += char

print('Encrypted message:', encrypted_message)
