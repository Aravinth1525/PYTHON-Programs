a=input("Enter The String : ")
b=a.find('$')
if (b!=-1):
    d=[b.replace('$',"@$") for b in a]
    e="".join(d)
    print(d)
    print('$'+e+'$')
else:
    print('$'+a+'$')
