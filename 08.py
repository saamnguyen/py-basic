#Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
#khi dinh nghia tham so instance thi can them no vao init
#co the khoi tao doi tuong ban cach truyen tham so hoac set gia tri sau

class Person:
    name = "Person"

    def __init__(self, name = None) :
        self.name = name

person1 = Person("Sam")
print("%s name is %s" % (Person.name, person1.name))

person2 = Person()
person2.name = "Sam Nguyen"
print("%s name is %s" % (Person.name, person2.name))