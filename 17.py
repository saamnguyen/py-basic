#Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

#Giả sử đầu vào là: Quản Trị Mạng

#Thì đầu ra là:

#Chữ hoa: 3

#Chữ thường: 8

x = input("Input: ")
y = {'upper': 0, 'lower': 0}

for i in x:
    if i.isupper():
        y['upper']+=1
    elif i.islower():
        y['lower']+=1

print('Upper: ', y['upper'])
print('Lower: ', y['lower'])