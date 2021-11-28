#viet chuong trinh chap nhan chuoi so, phan tach bang dau phay
#tao ra mot danh sach va mot tuple chua moi so
#input 34, 67, 55, 33, 12, 98
#output: ['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

x = input("Nhap gia tri: ")
l = x.split(',')
t = tuple(l)
print(l)
print(t)
