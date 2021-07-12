from abc import ABCMeta


a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))

if a>b and a>c :
    print("A Is Greater")
if b>a and b>c :
    print("B Is Greater")
if c>a and c>b :
    print("C Is Greater")
if a<b and a<c :
    print("A Is Lowest")
if b<a and b<c :
    print("B Is Lowest")
if c<a and c<b :
    print("C Is Lowest ")