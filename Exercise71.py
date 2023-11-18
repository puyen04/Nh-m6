x = float(input("Enter a number to find its square root: "))
guess = x / 2

while abs(guess * guess - x) > 10**(-12):  
    guess = (guess + x / guess) / 2  

print("The square root of", x, "is approximately" ,guess)