number = int(input("Enter a number to see its multiplication table:"))
numbers = range(1, 11)

for product in numbers:
    print(f"{number} * {product} = {number * product}")
    product += 1