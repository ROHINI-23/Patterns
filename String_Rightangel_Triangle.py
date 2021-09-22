str1 = str(input("Enter the string value: "))

n = len(str1)
k = 0
for i in range(0,n):
    for j in range(0,k+1):
        print(str1[j],end = " ")
    k = k+1
    print()

k = 0
for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,k+1):
        print(str1[j],end = " ")
    k = k+1
    print()
print("_______________________________________________________________")


k = n
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,k):
        print(str1[j],end = " ")
    k = k-1
    print()


k = n
for i in range(n,0,-1):
    for j in range(0,k):
        print(str1[j],end = " ")
    k = k-1
    print()
