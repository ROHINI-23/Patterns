n = int(input("Enter the number of rows: "))

k = 0
for i in range(0,n):
    for j in range(0,k+1):
        print(j+1, end =" ")
    k = k + 1
    print()

print("____________________________________________________________________")

k = 0
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=' ')
    for j in range(0,k+1):
        print(j+1, end= " ")
    k = k+1
    print()

print("______________________________________________________________________")

k = n
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,k):
        print(j+1,end=" ")
    k = k-1
    print()

print("_______________________________________________________________________")

k = n
for i in range(n,0,-1):
    for j in range(0,k):
        print(j+1,end=" ")
    k = k - 1
    print()