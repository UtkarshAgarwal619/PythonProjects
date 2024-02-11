stri=int(input("Enter a number:"))
#if stri==stri[::-1]:
#    print("Palindrome")
#else:
#    print("Not a palindrome")

rev=0
x=stri
while(stri>0):
    rev=(rev*10)+stri%10
    stri=stri//10
if(x==rev):
    print("Is Palindrome")
else:
    print("Not Palindrome")
