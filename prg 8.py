n=input("enterthe name:")
a=int(input("enter the age:"))
g=input("enter sex: 'M or f' :")
d=int(input("enter the numberof days :"))
if(a>18 and a<=30 and g=="m"):
    print("your wages is :",700*d)
elif(a>18 and a<=30 and g=="f"):
    print("your wages is :",750*d)
elif(a>30 and a<=40 and g=="m"):
    print("your wages is :",800*d)
elif(a>30 and a<=40 and g=="f"):
    print("your wages is :",800*d)
else:
    print("invalid entry")
    