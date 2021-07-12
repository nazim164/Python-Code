



class Myclass ():
    def show(self):
      
        name=(input("Enter Student Name :"))
        roll=int(input("Enter Student Roll No :"))
        s1=int(input("Enter Student Subject S1 :"))
        s2=int(input("Enter Student Subject S2 :"))
        s3=int(input("Enter Student Subject S3 :"))
        s4=int(input("Enter Student Subject S4 :"))
        s5=int(input("Enter Student Subject S5 :"))

        total=s1+s2+s3+s4+s5
        per=total/5
        if s1>=40 and s2>=40 and s3>40 and s4>=40 and s5>40 and per>=50 :
            result="Pass"
        else :
            result="Fail"
        if per<50 and result=="Fail" :
                Grade="****"
        elif per<=50 and  per>65 and result=="Paass" :
                Grade="C"
        elif per>=65 and per<75 and result=="Pass":
                Grade="B"
        elif per>=75 and per<85 and result=="Pass":
                Grade="A"
        elif per>=85 and result=="Pass":
                Grade="A+"
        else:
            
                Grade="*******"
        print("Student Name : ",name,"!!!!!","Student Roll No :",roll)
        print("Subject S1 :",s1,"!!!!!","Subject S2 :",s2,"!!!!!","Subject S3 :",s3,"!!!!!","Subject S4 :",s4,"!!!!!","Subject S5 :",s5)
        print("Total Of Student :",total,"!!!!!","Percentage Of Student :",per)
        print("Student Result :",result,"!!!!!","Student Grade :",Grade)

m1=Myclass()
m1.show()

