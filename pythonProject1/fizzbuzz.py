#Given an integer n, return a string array answer (1-indexed)
#where:
#answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#answer[i] == "Fizz" if i is divisible by 3.
#answer[i] == "Buzz" if i is divisible by 5.
#answer[i] == i if non of the above conditions are true.

n=input("Enter a number:")
for n in range(1,10):
    if n%5==0 and n%3==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(True)