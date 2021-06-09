a=input("Enter The String : ")
c=list(a)
b=a.find('$')
if (b!=-1):
    d=[b.replace('$',"@$") for b in c]
    e="".join(d)
    print('$'+e+'$')
else:
    print('$'+a+'$')