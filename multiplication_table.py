number = int(input("Enter a number to see its multiplication table:"))
numbers = range(1, 11)

for product in numbers: #for loop iterating from 1 to 10
    print(f"{number} * {product} = {number * product}")
    product += 1