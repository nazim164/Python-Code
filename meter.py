class Myclass():
    def show(args):
        

        name=(input("Enter Customer Name :"))
        meter_no=int(input("Enter Meter No :"))
        initail_r=float(input("Enter Initial Riding :"))
        final_r=float(input("Enter Final Riding :"))
        total_unit=final_r-initail_r
        type_of_cus=(input("Enter Type Of  Customer :"))

        if type_of_cus=="Residential":
            total_bil=total_unit*3.50
        elif type_of_cus=="Agriculture":
            total_bil=total_unit*2.50
        elif type_of_cus=="Commercial":
            total_bil=total_unit*6.50
        if total_bil>=8000:
            charge=total_bil*0.10
            total_bil=total_bil+charge



        print("Custmer Name :",name,"Meter No :",meter_no)
        print("Final Riding :",final_r,"Initial Riding : ",initail_r)
        print("Type Of Customer :",type_of_cus)
        print("Total Unit :",total_unit,"Total Bill :",total_bil)

m1=Myclass()
m1.show()