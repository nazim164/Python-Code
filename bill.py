itemame=(input("  Item Name :"))
price=int(input("  Price :"))
Qaunt=int(input("  Qauntity :"))

total=price*Qaunt
dis=total*0.05
netprice=total-dis
print("!!!!!!!!!!!!!!!! TOTAL BILL IS")
print("Total Is :",total)
print("Discount Is :",dis)
print("NetPrice Is :",netprice)