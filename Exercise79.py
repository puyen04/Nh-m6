import random

# Chọn số nguyên ngẫu nhiên đầu tiên từ 1 đến 100
maximum = random.randint(1, 100)
update_count = 0

print(maximum)

# Tạo 99 số nguyên ngẫu nhiên và kiểm tra số lớn nhất
count = 1
while count < 100:
    new_number = random.randint(1, 100)
    count += 1
    
    print(new_number, end=' ')
    
    if new_number > maximum:
        maximum = new_number
        update_count += 1
        print("<== Update", end=' ')
    print()

print("\nThe maximum value found was", maximum)
print("The maximum value was updated", update_count,"time")
