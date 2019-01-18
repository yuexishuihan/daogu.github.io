class Student():
    sum = 0
    # name = ''  
    # age = 0
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        self.__class__.sum += 1
        print('当前班级学生人数为：'+str(self.__class__.sum) )

    def do_homework(self):
        print('homework!')

    @classmethod
    def plus_lsum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x,y):
        print('This is a static method')

student1 = Student('sdj',11)
