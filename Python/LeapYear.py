try:
    y=int(input("Enter the year : "))
    if(y%4==0):
        if(y%100==0):
            if(y%100==0):
                print("{0} is a Leap Year".format(y))
            else:
                print("{0} is not a Leap Year".format(y))
        else:
            print("{0} is a Leap Year".format(y))
    else:
        print("{0} is not a Leap Year".format(y))
except:
    print("Enter the Year : ")