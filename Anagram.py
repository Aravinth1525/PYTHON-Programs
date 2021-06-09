def check():
    a=input("\nEnter the First word : ")
    b=input("Enter the Second word : ")
    if(sorted(a.lower())==sorted(b.lower())):
        print("\nThese words are ANAGRAM")
    else:
        print("These words are not ANAGRAM")
i=0
x=int(input("For how many pairs you want to check Anagram : "))
for i in range(0,x):
    check()