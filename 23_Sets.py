a = {1,1,2,3,4,5}
print(a) #Does not Print Repeated Items

b={} #This is an Empty Dictionary
c=set() #This is an Empty Set

#Adding Values
c.add(1) #Only Hashable i.e. Non-Changing things can be added i.e TUPLES Can be added but, LIST DICTIONERY Cant be Added
print(c)

#Length
print(len(a))

#Remove
print(a.remove(5)) # Remove the Chosen Value

#Pop
print(c.pop()) #Pops out Arbitary i.e. Non-Chosen Value

#Clear
print(a.clear()) #Empties the set
