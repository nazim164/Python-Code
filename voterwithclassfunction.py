class Show():
    def dis(self):
        name=(input("Enter Voter Name :"))
        age=int(input("Enter Voter Age :"))
        if age>=18 :
            print("You Are Eligible For Vote")
        else :
            print("Sorry .... You Are Not Eligible For Vote")
f1=Show()
f1.dis()
        