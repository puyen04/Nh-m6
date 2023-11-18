
print("   ", end="")
for i in range(1, 11):
    print(str(i), end="   ")
print("\n")


for i in range(1, 11):
    print(str(i), end="  ")
    for j in range(1, 11):
        product = i * j
        if product < 10:
            print(" ", end="")
        print(str(product), end="  ")
    print()
