from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")

class Children(StudentBase):
    def study(self):
        print("재미나게 놀기")

    def go_to_school(self):
        print("유치원가기")

    def sleep(self):
        print("낮잠 자기")

james = Student()
james.study()
james.go_to_school()

print("-------------")

obj = Children()
obj.study()
obj.go_to_school()
obj.sleep()

lst = []
lst.append(obj)
lst.append(james)

print(lst)

for data in lst:
    data.study()
    data.go_to_school()