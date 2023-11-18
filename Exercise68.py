bits = input("Enter an 8-bit string (or enter a blank line to finish): ")

while bits: 
    if len(bits) != 8 or not bits.isdigit():  
        print("Error: Incorrect format (requires 8 bits).")
    else:
        count_ones = bits.count('1')  
        
        if count_ones % 2 == 0:  
            print("The even parity bit will be 0.")
        else: 
            print("The even parity bit will be 1.")
    
    bits = input("Enter an 8-bit string (or enters a blank line to finish): ")  

print("End of the program.")
