my_list=[1,2,3,4,5,6]
def square(num):
    return num**2
for item in map(square,my_list):
    print(item)