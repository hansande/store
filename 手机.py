import time


class oldphone():
    _brand = ""
    _phoneNumber = ""
    _voice = ""

    def setbrand(self, brand):
        self._brand = brand

    def getbrand(self):
        return self._brand

    def setphoneNumber(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def getphoneNumber(self):
        return self._phoneNumber

    def setvoice(self, voice):
        self._voice = voice

    def getvoice(self):
        return self._voice

    def show(self):
        print("你的手机品牌为", self._brand, "正在打电话给", self._phoneNumber, "你的音乐为", self._voice)


class NewPhone(oldphone):
    _address = ""
    _picture = ""
    _mic = False
    _call = ""

    def setaddress(self, address):
        if address == "日本":
            print("小鬼子死啦死啦的")
        else:
            self._address = address

    def getaddress(self):
        return self._address

    def setpicture(self, picture):
        self._picture = picture

    def getpicture(self):
        return self._picture

    def setcall(self, call):
        self._call = call

    def getcall(self):
        return self._call

    def show(self):
        print("你正在拨打", self._call, "你的归属地为", self._address, "大头贴为", self._picture, "已经开启录音功能,正在连接")
        for i in range(8):
            print(".", end="")
            time.sleep(1)
        print("本次通话完成[5:36]！")
        print("通话结束.5.67")


p = NewPhone()
p.setaddress("中国")
p.setpicture("奥特曼")
p.setcall(13716035532)
p.show()
