'''
Có rất nhiều cụm từ trở thành đối xứng khi bỏ qua khoảng cách. 
Các ví dụ bao gồm “chó, đi”, “hãy chạy đến chỗ tôi yêu tinh xa xôi” và “một vài ng đàn ông giải thích 9 bản ghi nhớ”, 
trong số nhiều ví dụ khác. 
Mở rộng lời giải của bạn cho Bài tập 72 để nó bỏ qua khoảng cách trong khi xác định xem một chuỗi có phải là một bảng màu hay không. 
Đối với một thử thách bổ sung, hãy mở rộng giải pháp của bạn 
để giải pháp đó cũng bỏ qua các dấu chấm câu và coi chữ hoa và chữ thường là tương đương.
'''

phrase = input('Phrase: ')

cleaned_phrase = ''.join(char.lower() for char in phrase if char.isalnum())

start_index = 0
end_index = len(cleaned_phrase) - 1
is_palindrome = True

while start_index < end_index:
    if cleaned_phrase[start_index] != cleaned_phrase[end_index]:
        is_palindrome = False
        break
    start_index += 1
    end_index -= 1

if is_palindrome:
    print('The phrase is a palindrome')
else:
    print('The phrase is not a palindrome')
