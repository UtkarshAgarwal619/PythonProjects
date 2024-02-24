string1=input("Enter string 1:")
string2=input("Enter string 2:")
string3=string1.lower()
string4=string2.lower()
if len(string3)!=len(string4):
    print("Not an anagram")
else:
    if sorted(string3)==sorted(string4):
        print("Anagram")
    else:
       print("Not an anagram")