n = int(input())

k = n
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,k):
        print("*", end=" ")
    k = k-1
    print()