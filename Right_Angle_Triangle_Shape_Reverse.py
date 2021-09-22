rows = int(input("Enter the number of rows:"))
k = 0
for i in range(0, rows):
    for j in range(0, rows - i - 1):
        print(" ", end=" ")
    for j in range(0, k + 1):
        print("*", end=" ")
    k = k + 1
    print()


