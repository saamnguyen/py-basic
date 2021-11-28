#Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) 
# (bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
#  Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, 
# được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy.

import math
C = 50
H = 30
values = []

#x for x cach ghi tat : nested    
items=[x for x in input("Nhập giá trị của d: ").split(',')]

#tuong tu nhu items tren
#items = []
#for x in input("Nhap gia tri: ").split(','):
#    items.append(x)


for d in items:
    values.append(str(int(round(math.sqrt(2 * C * float(d) / H)))))

print(','.join(values))

text = "word1anotherword23nextone456lastone333"
numbers = [x for x in text if x.isdigit()]
print(numbers)