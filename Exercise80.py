'''
Bạn phải tung đồng xu tối thiểu bao nhiêu lần trước khi có thể có ba lần tung đồng xu liên tiếp dẫn đến cùng một kết quả
(cả ba đều là mặt ngửa hoặc cả ba đều là mặt sấp)? Có thể cần tối đa bao nhiêu lần lật nhà? Trung bình cần bao nhiêu lần lật?
Trong bài tập này, chúng ta sẽ khám phá những câu hỏi này bằng cách tạo ra một chương trình mô phỏng một số chuỗi lần tung đồng xu.
Tạo một chương trình sử dụng trình tạo số ngẫu nhiên của Python để mô phỏng việc tung đồng xu nhiều lần. 
Đồng xu mô phỏng phải công bằng, nghĩa là xác suất mặt ngửa bằng xác suất mặt sấp. 
Chương trình của bạn sẽ tung đồng xu mô phỏng cho đến khi xuất hiện 3 mặt ngửa liên tiếp hoặc 3 mặt sấp liên tiếp. 
Hiển thị chữ H mỗi khi kết quả là mặt ngửa và chữ T mỗi khi kết quả là mặt sấp, với tất cả các kết quả được hiển thị trên cùng một dòng. 
Sau đó hiển thị số lần lật cần thiết để đạt được 3 lần lật liên tiếp với cùng một kết quả. 
Khi chương trình của bạn chạy, nó sẽ thực hiện mô phỏng 10 lần và báo cáo số lần lật trung bình cần thiết. 
Đầu ra mẫu được hiển thị dưới đây:
H T T T (4 lần lật)
H H T T H T H T T H H T H T T H T T T (19 lần lật)
T T T (3 lần lật)
T H H H (4 lần lật)
H H H (3 lần lật)
T H T T H T H T T H H T H T H H H (18 lần lật)
H T T H H H (6 lật)
T H T T T (5 lần lật)
T T H T T H T H T H H H (12 lần lật)
T H T T T (5 lần lật)
Trung bình cần 7,9 lần lật.
'''

import random

total_flips = 0
simulations = 10

for _ in range(simulations):
    consecutive_flips = 0
    flips_needed = 0

    while consecutive_flips < 3:
        flip_result = random.choice(['H', 'T'])
        print(flip_result, end=' ')
        flips_needed += 1

        if flip_result == 'H':
            consecutive_flips = (consecutive_flips + 1) if consecutive_flips >= 0 else 1
        else:
            consecutive_flips = (consecutive_flips - 1) if consecutive_flips <= 0 else -1

    print(f"({flips_needed} flips)")
    total_flips += flips_needed

average_flips = total_flips / simulations
print(f'\nOn average, {average_flips:.1f} flips were needed.')