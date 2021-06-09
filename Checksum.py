def binary_add(a,b):
    max_len = max(len(a), len(b)) 
    a = a.zfill(max_len) 
    b = b.zfill(max_len) 
    result = '' 
    carry = 0
    for i in range(max_len -1, -1, -1): 
        r = carry 
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result  
        carry = 0 if r < 2 else 1
    if carry != 0: 
        result = '1' + result
    return result
l=[]
total=0
print("\nAravinth R - 19MIC0053")
print("\nLab CAT")
print("\nProblem - Checksum")
n=int(input("\nEnter number of inputs : "))
print("")
for i in range (n):
    l.append(int(input("Enter the number : ")))
for j in range (0,len(l)):
    total=total+l[j]
print("\nSum of the numbers : ",total)
l.sort()
maximum=l[-1]
binary=bin(maximum)[2:]
x=len(binary)
sum = bin(total)[2:]
last= sum[len(sum)-x:]
first= sum[:(len(sum)-x)]
final = binary_add(last,first)
while(len(final)>x):
    last = final[(len(final)-x):]
    first = final[:(len(final)-x)]
    final = binary_add(last,first)
print("\nWrapped Sum : "+final+"\n")
final1 = final.replace('1', '%temp%').replace('0', '1').replace('%temp%', '0')
print("1's Complement : "+final1)

final2 = int(final1)
decimal, i, n = 0,0,0
while(final2 != 0): 
    dec = final2 % 10
    decimal = decimal + dec * pow(2, i) 
    final2 = final2//10
    i += 1
print("\nChecksum Result : ",decimal,"\n")
