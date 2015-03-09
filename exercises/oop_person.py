# oop_person.py
# Object-Oriented Programming
# Python, Ruby, Java, C++, Objective-C

# vs imperative / procedural

# class - analogous to data type
# int a
# shape x, y, z (objects)
# class has both data and methods
# eg shape - data (point[x,y]), method (move[m,n])

# person
# data - name, weight, height
# methods
# - constructor: Person() - allocate memory and create object
# - accessor/getty: read data
# - modifier/mutator/setty: change data
# - helper / support: perform utility function
# - destructor: ~Person() - free memory and destroy object

# a class is a blueprint/template for objects
# object is an instanace of a class
# class - Person
# objects - p1 (Mr Thng), p2 (Mr Leong), p3 (Mr Fan)

# encapsulation
# - class bundles data and methods
# - use public methods to access private data
# inheritance - code reuse
# - subclass will inherit superclass data and methods
# - subclass can create its own data and methods
# polymorphism
# - ability to invoke different class methods using same name
# - appropriate method will be bound dynamically at runtime

class Person:
    # constructor
    def __init__(self, nName, nWeight, nHeight):
        self.__name = nName
        self.__weight = nWeight
        self.__height = nHeight

    # accessors
    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height    

    # modifers
    def set_weight(self, newWeight):
        self.__weight = newWeight

    def eat(self, addWeight):
        #self.__weight = self.__weight + addWeight
        self.__weight += addWeight

    def shit(self, remWeight):
        self.__weight = self.__weight - remWeight

    def set_height(self, newHeight):
        self.__height = newHeight

    def sleep(self, addHeight):
        self.__height = self.__height + addHeight

    # helper/support
    def display(self):
        print(self.__name)
        print(self.__weight)
        print(self.__height)

    def bmi(self):
        return self.__weight / (self.__height * self.__height)


class Student(Person):

    # constructor
    def __init__(self, nName, nWeight, nHeight, nClassid):
        super().__init__(nName, nWeight, nHeight)
        self.__classid = nClassid

    # accessor
    def get_classid(self):
        return self.__classid

    # modifier
    def set_classid(self, newClassid):
        self.__classid = newClassid

    # helper / support
    def display(self): # overriding
        super().display()
        print(self.__classid)


class Staff(Person):

    # constructor
    def __init__(self, nName, nWeight, nHeight, nDepartment):
        super().__init__(nName, nWeight, nHeight)
        self.__department = nDepartment

    # accessor
    def get_department(self):
        return self.__department

    # modifier
    def set_department(self, newDepartment):
        self.__department = newDepartment

    # helper/support
    def display(self):
        super().display()
        print(self.__department)

# main
stud1 = Student("Mr Li", 60, 1.75, "5C23")
#stud1.display()

staff1 = Staff("Boss Pang", 57, 1.60, "Computing")
#staff1.display()

school = []
school.append(stud1)
school.append(staff1)

for user in school:
    user.display() # code generality

##p1 = Person("Mr Fan", 67, 1.65)
##p1.display()
##p1.eat(5)
##p1.sleep(0.02)
##p1.shit(3)
##p1.display()
###print(p1.get_name())
###print(p1.get_weight())
###print(p1.get_height())
###p1.display()
###print(p1.bmi())
###p1.set_weight(63)
###print(p1.get_weight())
###print(p1.bmi())
###print(p1.name)
###print(p1.weight)
###print(p1.height)
##        
##p2 = Person("Mr Leong", 58, 1.75)
###print(p2.name)
###print(p2.weight)
###print(p2.height)
##
##p3 = Person("Mr Thng", 62, 1.73)
###print(p3.name)
###print(p3.weight)
###print(p3.height)











