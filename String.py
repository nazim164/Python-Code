str=(input("Enter Your String :"))
newstr=''
count1=0
count2=0
count3=0

for i in str:
    if (i.isupper())==True:
        count1+=1
        newstr+=(i.lower())
    elif (i.islower())==True:
        count2+=1
        newstr+=(i.upper())
    elif(i.isspace())==True:
        count3+=1
        newstr+=i

print("In Orignal String ")
print("Uppar Case String Is :",count1)
print("Lower Case String Is :",count2)
print("Spaces In String Is :",count3)
print("After Changing The Cases :",newstr)