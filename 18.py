#Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.

#Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234

a = input("Nhập số a: ")
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
# Bài tập Python 18, Code by Quantrimang.com
print ("Tổng cần tính là: ",n1+n2+n3+n4)
print(type(n1))