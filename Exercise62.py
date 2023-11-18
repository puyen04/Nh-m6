# Các giá sản phẩm
price1 = 4.95
price2 = 9.95
price3 = 14.95
price4 = 19.95
price5 = 24.95

# Tỷ lệ giảm giá
discount_rate = 0.6  # 60% discount

print("Original Price | Discount Amount | New Price")

for i in range(1,6):  # Số lượng sản phẩm từ 1 đến 5
    if i == 1:
        discount_amount = price1 * discount_rate
        new_price = price1 - discount_amount
        print(price1,"        |   ",round(discount_amount,2),"           |   ",round(new_price,2))
    elif i== 2:
        discount_amount = price2* discount_rate
        new_price = price2- discount_amount
        print(price2,"        |   ",round(discount_amount,2),"           |   ",round(new_price,2))
    elif i == 3:
        discount_amount = price3 * discount_rate
        new_price = price3 - discount_amount
        print(price3,"        |   ",round(discount_amount,2),"           |   ",round(new_price,2))
    elif i== 4:
        discount_amount = price4 * discount_rate
        new_price = price4- discount_amount
        print(price4,"        |   ",round(discount_amount,2),"           |   ",round(new_price,2))
    else:
        discount_amount = price5 * discount_rate
        new_price =price5- discount_amount
        print(price5,"        |   ",round(discount_amount,2),"           |   ",round(new_price,2))
    
    
    

    
   
