def pair(a,sum):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if(a[i]+a[j]==sum):
                print("\nPair found at indices ",i," and ",j)
                return


    print("\nPair not found")
a=[]
x=int(input("Enter the number of elements : "))
for k in range(0,x):
    y=int(input("Enter the element : "))
    a.append(y)
print("\nThe list is ",a)

sum=int(input("\nEnter the sum of the Pair : "))
pair(a,sum)