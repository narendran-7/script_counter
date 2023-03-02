# print("hello world")

f = open("own.txt","r")
val = int(f.read())
val +=1
f.close()

f = open("own.txt","w")
f.write(str(val))
print("----------> ",val)
f.close()

# class Distruct:
#     def __init__(self):