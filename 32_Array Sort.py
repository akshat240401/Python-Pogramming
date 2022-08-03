print("Input Array Elements:")
l=list(map(int,input().split(" ")))
l.sort()
a=[0 for i in range(len(l))]
print("Input your choice:")
print("1.Arrange the Array in Ascending Order")
print("2.Arrange the Array in Descending Order")
c=int(input("Choice(1/2):"))
if(c==1):
    for i in range(len(l)):
        print(l[i],end=" ")
elif(c==2):
    for i in range(len(l)):
        a[len(l)-1-i]=l[i]
    for i in range(len(a)):
        print(a[i],end=" ")
else:
    print("Choose either 1 or 2.")