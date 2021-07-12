class Myclass() :
    def show(self) :
  
       
        a=int(input("Enter First Number :"))
        b=int(input("Enter Second Number :"))
        c=int(input("Enter Third Number :"))
        if a>b and a>c :
            print("A Is Greater !!!!")
        elif b>a and b>c :
            print("B Is Greater !!!")
        else :
            print("C Is Greaterc!!!")
    def name(self):
                x=int(input("Enter First Number :"))
                y=int(input("Enter Second Number :"))
                z=int(input("Enter Third Number"))
                if x<y and x<z :
                    print("X Is Lowest ")
                elif y<x and y<z :
                    print("Y Is Lowest ")
                else :
                    print("Z Is Lowest")


        

next=Myclass()
next.show()
next.name()


