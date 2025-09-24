size = int(input("nter the size of the pattern:"))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1