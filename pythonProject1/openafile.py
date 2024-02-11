def sum(a,b):
    return a+b
def write(filename,content):
    with open(filename,'w') as file:
        file.write(content)
filename="file.txt"
content="This is example file"
write(filename,content)
