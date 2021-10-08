# class glass:
#     _high=""
#     _broad=""
#     _cubage=""
#     _cap=""
#     def sethight(self,high):
#         if high<=0:
#             print("你输入的数据有误,别瞎弄")
#         else:
#             self._high=high
#     def gethight(self):
#         return self._high
#     def setbroad(self,broad):
#         if broad<=0:
#             print("你输入的数据有误,别瞎弄")
#         else:
#             self._broad=broad
#     def getbroad(self):
#         return self._broad
#     def setcubage(self,cubage):
#         if cubage<0 or cubage>10000:
#             print("你输入的数据有误,别瞎弄")
#         else:
#             self._cubage =cubage
#     def getcubage(self):
#         return self._cubage
#     def setcap(self,cap):
#         self._cap=cap
#     def getcap(self):
#         return self._cap
#     def showme(self):
#      print("这个杯子为",self._high,"厘米,宽为",self._broad,"他的入口是",self._cap,"他的容积是",self._cubage)
#
# p=glass()
# p.sethight(20)
# p.setbroad(2)
# p.setcap("方的")
# p.setcubage(15)
# p.showme()

class computer:
    _screen = ""
    _price = ""
    _cup = ""
    _memory = ""
    _time = ""

    def setscreen(self, screen):
        if screen < 0 or screen > 10:
            print("你输的数据错误,别瞎搞")
        else:
            self._screen = screen

    def getscreen(self):
        return self._screen

    def setprice(self, price):
        if price < 1000 or price > 30000:
            print("你的电脑没有这么值钱,别瞎搞")
        else:
            self._price = price

    def getprice(self):
        return self._price

    def setcup(self, cup):
        self._cup = cup

    def getcup(self):
        return self._cup

    def setmemory(self, memory):
        if memory < 0 or memory > 1000:
            print("滚吧哪里有这么输入的")
        else:
            self._memory = memory

    def getmemory(self):
        return self._memory

    def settime(self, time):
        if time < 0 or time > 100:
            print("你的电脑真牛逼")
        else:
            self._time = time

    def gettime(self):
        return self._time

    def show(self):
        print("你的电脑屏幕为", self._screen, "你的电脑是", self._price, "买的,电脑是", self._cup, "的,内存为", self._memory, "待机时长为",
              self._time)


p = computer()
p.setscreen(6.75)
p.setprice(10000)
p.setcup("i7")
p.setmemory(500)
p.settime(90)
p.show()
