#Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, 
# kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

#Ví dụ đầu vào là: 0100,0011,1010,1001

#Đầu ra sẽ là: 1010

a = []

items = [x for x in input("Nhap: ").split(',')]

for p in items:
    intp = int(p, 2)# convert thanh so binh thuong
    print(intp)
    if not intp % 5:
        a.append(p)

print(', '.join(a))