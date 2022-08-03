n1 = int(input("Enter marks for subject 1- "))
n2 = int(input("Enter marks for subject 2- "))
n3 = int(input("Enter marks for subject 3- "))

total=n1+n2+n3/3<40
if(n1<33 or n2<33 or n3<33):
    print("FAILED")
if((n1+n2+n3/3)<40):
    print("FAILED")
else:
    print("passed")
