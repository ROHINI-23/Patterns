n = int(input())
k = 0
for i in range(0,n):
    for j in range(0,k+1):
        print(1+k, end=" ")
    k = k+1
    print()