n = int(input())

lis = []

for i in range(0,n):
    temp = []
    for j in range(0,i+1):
        if j==0 or j ==i:
            temp.append(1)
        else:
            temp.append(lis[i-1][j-1] + lis[i-1][j])
    lis.append(temp)

print(lis)

k = 0
for i in range(0,n):
    for j in range(0,n-i-1):
        print(format(" ","<5"),end=" ")
    for j in range(0,k+1):
        print(format(lis[i][j],"<11"),end=" ")
    k = k+1
    print()