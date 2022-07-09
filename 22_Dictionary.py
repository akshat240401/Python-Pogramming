myDict={"Name":"Akshat","Profession":"Student","Marks":[10,11,12],"subDict":{"NickName":"Aki","Hobby":"Cricket"}}
# print(myDict["Name"])
print(myDict['subDict']['Hobby'])

myDict["Marks"]=[100,100,100] #It is Mutable
print(myDict)

print(myDict.keys()) #Prints Keys
print(myDict.values()) #Prints Values
print(myDict.items()) #Prints (Key,Value) Pair
updateDict={
    "Greeting":"Hello"
}
myDict.update(updateDict) #Updates new values as well as existing values
print(myDict)

print(myDict.get("Name")) #Prints Value Associated to key Name
print(myDict("Name")) #Prints Value Associated to key Name

print(myDict.get("Name100")) #Returns None as Name100 key is not present
print(myDict("Name100")) #Returns ERROR as Name100 key is not present