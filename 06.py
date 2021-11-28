#Viết một method tính giá trị bình phương của một số.

x = int(input("input: "))

def square(x):
    return x ** 2

def square1(x):
    return pow(x, 2)

def square2(x):
    return x * x

print(square(2))
print(square(x))
print(square1(2))
print(square2(2))