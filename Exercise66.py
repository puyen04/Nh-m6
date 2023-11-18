'''
Bài tập 51 bao gồm một bảng thể hiện sự chuyển đổi từ điểm chữ sang điểm trung bình 
tại một tổ chức học thuật cụ thể. Trong bài tập này, bạn sẽ tính điểm trung bình của
một số lượng điểm chữ tùy ý được nhập bởi người dùng. Người dùng sẽ nhập một dòng 
trống để cho biết tất cả các điểm đã được cung cấp. Ví dụ, nếu người dùng nhập A, 
tiếp theo là C+, tiếp theo là B, và cuối cùng là một dòng trống, thì chương trình 
của bạn nên báo cáo điểm trung bình là 3.1.

Bạn có thể tận dụng giải pháp của mình cho Bài tập 51 khi hoàn thành bài tập này. 
Chương trình của bạn không cần thực hiện bất kỳ kiểm tra lỗi nào. Nó có thể giả 
định rằng mỗi giá trị được nhập bởi người dùng luôn là một điểm chữ hợp lệ hoặc 
một dòng trống.
Điểm hệ chữ 	Điểm GPA ở Canada       Xếp loại
A+	                4	                Xuất sắc
A	                3.9	
A-	                3.7	
B+	                3.3	                Giỏi
B	                3	    
B-	                2.7 
C+	                2.3	            	Khá
C	                2	    
C-	                1.7	    
D+	                1.3	            	Trung bình
D	                1	    
D-	                0.7 
E/F	                0	                Không đạt
'''

tongdiem=0
somonhoc=0
while True:
    diemchu=input('Enter scores in words:')
    if diemchu=='':
        break
    elif diemchu=='A+':
        so=4
    elif diemchu=='A':
        so=3.9
    elif diemchu=='A-':
        so=3.7
    elif diemchu=='B+':
        so=3.3
    elif diemchu=='B':
        so=3
    elif diemchu=='B-':
        so=2.7
    elif diemchu=='C+':
        so=2.3
    elif diemchu=='C':
        so=2
    elif diemchu=='C-':
        so=1.7
    elif diemchu=='D+':
        so=1.3
    elif diemchu=='D':
        so=1
    elif diemchu=='D-':
        so=0.7
    elif diemchu=='E' or diemchu=='F':
        so=0        
    else:
        print('Please re-enter')
    tongdiem=tongdiem+so
    somonhoc=somonhoc+1
if somonhoc>0:
    dtb=tongdiem/somonhoc
    print('Medium score:',round(dtb,1))
else:
    print('Not eligible for scoring')
