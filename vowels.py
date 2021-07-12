str=(input("Enter A String :"))
vowel=0
consonant=0
for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel+=1
    else:
        consonant+=1

print("Number Of Wovels :",vowel,"Number Of Consonant",consonant)

str1=(input("Enter The String :"))
print("Orignal String :",str1)
print("UpperCase String :",str1.upper())
print("LowerCase String :",str1.lower())
print("Capatalize String :",str1.capitalize())