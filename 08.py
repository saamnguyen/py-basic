class Person:
    name = "Person"

    def __init__(self, name = None) :
        self.name = name

person1 = Person("Sam")
print("%s name is %s" % (Person.name, person1.name))

person2 = Person()
person2.name = "Sam Nguyen"
print("%s name is %s" % (Person.name, person2.name))