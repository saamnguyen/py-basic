#Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, 
# chuyển các dòng này thành chữ in hoa và in ra màn hình. Giả sử đầu vào là:

#ello world
#Practice makes perfect

#Thì đầu ra sẽ là:

#HELLO WORLD
#PRACTICE MAKES PERFECT

lines = []

while True:
    s = input("Nhap: ")

    if s:
        lines.append(s.upper())
    else:
        break

for a in lines:
    print(a)