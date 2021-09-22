# dict={"老牛湾":"还可软"}
# print(dict["还可软"])

# a=20
# b=3
# c=2
# day=0
# while True:
#         a-=b
#         if a<0:
#             break
#         a+=c
#         day+=1
# print(day)


#
import  random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={12345678: {'username': 'xh','password': 123456, 'country': '中国', 'province': '陕西', 'street': '001', 'door': '002', 'money': 100},
      12345677: {'username': 'hc','password': 123456, 'country': '中国', 'province': '陕西', 'street': '001', 'door': '002', 'money': 100}}


bank_name="中国工商银行昌平支行"#全局变量
def bank_adduser(username,password,country,province,street,door,account,money):
    if account in bank :#如果一个变量在容器内就运行代码
        return 2
    if len(bank)>=100:
        return 3
    bank[account]={
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":中国工商银行昌平支行
    }
    return 1

    def useradd():
     username=input("请输入您的用户名：")
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    bankadd=bank_adduser(username,password,country,province,street,door,account,money)
    if bankadd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))
    elif bankadd ==2:
        print("用户已存在")
    elif bankadd == 3:
       print("数据库已满")













# 获取存钱的账户信息
def cun():
        acc=int(input("请输入要存钱的账号:"))
        if acc in bank:
                cun=int(input("请输入要存入的金额"))
                bank[acc]["money"]=bank[acc]["money"]+cun
                print("存入成功")
                print(bank[acc]["money"])

        else:
                print("账户错误")
                return False
# 获取取钱信息
def qu():
      acc=int(input("请输入取钱的账号"))
      if acc in bank:
        pwd=int(input("请输入密码"))
        if pwd!=bank[acc]["password"]:
                   print("密码不正确")
        elif pwd==bank[acc]["password"]:

            p = int(input("请输入取出的钱数"))
            if p<=bank[acc]["money"]:
                bank[acc]["money"]=bank[acc]["money"]-p
                print("取出成功")
                print(bank[acc]["money"])
            else:
                print("钱不够")
      else:
          print("账号不存在")
# 账户
def zhuanzhang():
    a=int(input("请输入转钱账户"))
    b=int(input("请输入收钱账户"))
    if a in bank and b in bank:
        pwda = int(input("请输入转钱账户密码:"))
        if pwda!=bank[a]["password"] :
                  print("密码错误")
        elif pwda==bank[a]["password"] :
           c=int(input("请输入你要转出的资金"))
           if c <= bank[a]["money"]:
               bank[a]["money"] = bank[a]["money"] - c
               bank[b]["money"] = bank[b]["money"] + c
               print("转账成功")
               print("转钱账户当前余额为:", bank[a]["money"])
               print("收钱账户当前余额为:", bank[b]["money"])
    else:
        print("账户不存在")

def chaxun():
    a=int(input("请输入你的账号"))
    if a in bank:
        b=int(input("请输入你的密码"))
        if b==bank[a]["password"]:
            print("进入成功,以下是你的信息")

            info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：*****
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
            print(info % (bank[a]["username"],a, b, bank[a]["province"], bank[a]["street"], bank[a]["door"], bank[a]["money"], bank_name))
        else:
            print("你输入的密码不正确")

    else:
        print("账号不存在")




















while True:
    begin = input("请选择业务")
    if begin == "1":
        print("开户")
        useradd()
    elif begin == "2":

        print("存钱")

        cun()

    elif begin == "3":
        print("取钱")
        qu ()
    elif begin == "4":
        print("转账")
        zhuanzhang()

    elif begin == "5":
        print("查询")
        chaxun()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break




