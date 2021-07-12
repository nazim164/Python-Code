name=(input("Enter Student Name :"))
roll=int(input("Enter Student Roll No :"))
s1=int(input("Enter S1 Marks :"))
s2=int(input("Enter S2 Marks :"))
s3=int(input("Enter S3 Marks :"))
s4=int(input("Enter S4 Marks :"))
s5=int(input("Enter S5 Marks :"))
total=s1+s2+s3+s4+s5
per=total/5

if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40 and per>=50 :
    result="Pass"
else :
    result="Fail"
if per<50 and result=="Fail" :
    Grade="*******"
elif per<=50 and per>65 and result=="Pass" :
    Grade="C"
elif per<=65 and per>75 and result=="Pass":
    Grade ="B"
elif per>=75 and per<85 and result=="Pass":
    Grade="A"
elif per>=85 and result=="Pass":
    Grade ="A+"
else :
    Grade="*****"
    
print("Student Name Is :",name,"Student Roll  No Is  :",roll)
print("Total Is :",total,"Percentage Is :",per)
print("Result Is  :",result,"Grade Is :",Grade)

