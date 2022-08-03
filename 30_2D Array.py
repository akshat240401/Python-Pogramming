row = int(input("Enter no. of rows - "))
column = int(input("Enter no. of columns - "))
# arr2 = [[0 for c in range(column)] for r in range(row)]
rval = (input("Input row val - "))
rval = rval.split(' ')
cval = (input("Input row cal - "))
cval = cval.split(' ')
arr2 = [[0 for cval in range(column)] for rval in range(row)]
for rval in range(row):
    for cval in range(column):
        arr2[rval][cval]=rval*cval
print(arr2)