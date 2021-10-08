class person:
    age=""
    sex=""
    name=""
class worker(person):
    def work(self):
        print("工人信息为",self.name,self.sex,self.age,"在工作")
class student(person):
    number=""
    def study(self,number):
        self.number=number
        print(self.name,self.sex,self.age,self.number,"开始学习")
    def ring(self,number):
        self.STUnumber = number
        print(self.name, self.sex, self.age, "开始唱歌")
worker=worker()
worker.age=40
worker.name="张大龙"
worker.sex="男"
worker.work()
stu=student()
stu.sex="男"
stu.age=20
stu.age=30
stu.study(input("请输入学号："))

