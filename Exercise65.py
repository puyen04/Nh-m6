import math


x_first = float(input(("Enter the x part of the coordinate: ")))

y_first = float(input(("Enter the y part of the coordinate: ")))


x_prev = x_first
y_prev = y_first
perimeter = 0.0

while True:
    print("Enter the x part of the coordinate (blank to quit): ", end="")
    x_input = input()
    if x_input == "":
        break
    x_current = float(x_input)
    
    print("Enter the y part of the coordinate: ", end="")
    y_input = input()
    y_current = float(y_input)

    dist = math.sqrt((x_current - x_prev)**2 + (y_current - y_prev)**2)
    perimeter += dist
    
    x_prev = x_current
    y_prev = y_current

perimeter += math.sqrt((x_first - x_prev)**2 + (y_first - y_prev)**2)

print("The perimeter of that polygon is ",perimeter)



















