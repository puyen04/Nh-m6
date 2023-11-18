'''
Một chuỗi là palindrome nếu nó giống nhau khi đọc từ trái sang phải và
từ phải sang trái. Ví dụ, "anna", "civic", "level" và "hannah" là tất 
cả các ví dụ về các từ palindrome. Viết một chương trình đọc một chuỗi 
từ người dùng và sử dụng một vòng lặp để xác định liệu chuỗi đó có phải 
là palindrome hay không. Hiển thị kết quả, bao gồm một thông báo đầu ra 
có ý nghĩa.
'''
# Nhập chuỗi từ người dùng
chuoi = input("input string: ")
nguoc=''
for i in range(len(chuoi)-1,-1,-1):
    nguoc=nguoc+chuoi[i]
if chuoi==nguoc:
    print('It is palindrome')
else:
    print('It is not palindrome')   