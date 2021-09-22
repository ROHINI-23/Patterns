"""Python Program to Print Right Angled Triangle Star Pattern"""
"""
n = int(input())
m = str(input())
for i in range(1, n + 1):
    print((m + " ") * i)
"""
rows = int(input("Enter the number of rows:"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end=" ")
    print()

rows = int(input("Enter the number of rows:"))
k = 0
for i in range(0, rows):
    for j in range(0, k+1):
        print("*", end=" ")
    k = k + 1
    print()

rows = int(input("Enter the number of rows:"))
for i in range(0,rows):
    for j in range(0,rows-i-1):
        print(" ",end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()