size = int(input("Enter the size of the pattern:"))  #prompt user for pattern size\]
if size <= 0:
    print("Enter a positive interger")
else:
    sizes = 0 

    while sizes < size:
        for col in range(size):
            print("*", end="")
        print()
        sizes += 1
