print("Enter the sides of triangles:")
a = int(input("Enter the side of a:"))
b = int(input("Enter the side of b:"))
c = int(input("Enter the side of c:"))

if a == b == c:
    print("Triangle is Equilateral")
elif a == b or b == c or c == a:
    print("Triangle is Isosceles ")
else:
    print("Triangle is Scalene")
