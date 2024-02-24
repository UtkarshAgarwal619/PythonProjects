vowels = 0
consonants = 0
string=input("Enter a string:")
vows='AEIOUaeiou'
for i in string:
    if i in vows:
        vowels +=1
    else:
        consonants +=1
print('Count Vowels:', vowels)
print('Count constant:', consonants)
