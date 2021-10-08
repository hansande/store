class kitchen:
    __name=""
    __age=""
    __zhufan=""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        if age>100 or age<0:
            print("你输入的年龄有误")
        else:
            self.__age=age
    def getage(self):
        return self.__age
    def setzhufan(self,zhufan):
        self.__zhufan=zhufan
    def getzhufan(self):
        return self.__zhufan
    def show(self):
        print("厨师的姓名为", self.__name, "年龄为", self.__age, "正在", self.__zhufan)

class cook1(kitchen):
    def cook(self):
        super().show()
        print("吵了一道炒菜,西红柿炒面")
class cook2(cook1):
    age=""
    name=""
cook=cook2()
cook.name="张家平"
cook.age=12
cook.setage(20)
cook.setname("小豆子")
cook.cook()
