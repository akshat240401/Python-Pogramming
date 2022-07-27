n1= int(input("Enter 1st number - "))
n2= int(input("Enter 2nd number - "))
n3= int(input("Enter 3rd number - "))
n4= int(input("Enter 4th number - "))

if(n1>n4):
    if(n1>n3):
        if(n1>n2):
            print("Greatest is -",n1)
elif(n2>n4):
    if(n2>n3):
        if(n2>n1):
            print("Greatest is -",n2)
elif(n3>n4):
    if(n3>n2):
        if(n3>n1):
            print("Greatest is -",n3)         
elif(n4>n3):
    if(n4>n2):
        if(n4>n1):
            print("Greatest is -",n4)       