x=int(input("enter the year:"))
if(x%400==0):
    if(x%4==0):
        print(x,"is the leap year")
    elif(x%100==0):
        print(x,"is not the leap year")
else:
    print(x,"is not the leap year")