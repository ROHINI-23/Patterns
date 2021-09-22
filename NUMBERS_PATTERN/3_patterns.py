n = int(input())
k = 0
for i in range(0,n):
    for j in range(k,-1,-1):
        print(1+j,end=" ")
    k = k+1
    print()