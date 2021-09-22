n = int(input())
k =0

for i in range(0,n-1):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,k+1):
        print("*",end=" ")
    k = k + 1
    print()

k = n
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,k):
        print("*", end=" ")
    k = k-1
    print()
