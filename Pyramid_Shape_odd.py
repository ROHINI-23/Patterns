n = int(input())
k = 0

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,2*k+1):
        print("1",end=" ")
    k = k + 1
    print()