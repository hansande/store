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
from mysql import update
from mysql import select
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
# bank={}

# bank={12345678: {'username': 'xh','password': 123456, 'country': '中国', 'province': '陕西', 'street': '001', 'door': '002', 'money': 100},
#       12345677: {'username': 'hc','password': 123456, 'country': '中国', 'province': '陕西', 'street': '001', 'door': '002', 'money': 100}}


bank_name="中国工商银行昌平支行"#全局变量
# def bank_adduser(username,password,country,province,street,door,account,money):
def bank_adduser(account, username, password, country, province, street, door, money):
    sql="select count(*) from users"
    param = []
    date = select(sql, param)
    sal1 = 'select * from users where account=%s'
    param1 = [account]
    date1 = select(sal1, param1)

    if len(date) > 100:
        return 3
    elif len(date1) > 0:
        return 2
    else:
        sal2 = 'insert into users(account, username, password, country, province, street, door, money)'
    ' values(%s,%s,%s,%s,%s,%s,%s,%s)'
    param2 = [account, username, password, country, province, street, door, money]
    update(sal2, param2)
    return 1

def useradd():
    username=input("请输入您的用户名：")#局部变量
    password = int(input("请输入密码："))#print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    bankadd=bank_adduser(account,username,password,country,province,street,door,money)
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
        print(info % (username, account, country, province, street, door, money, bank_name))
    elif bankadd ==2:
        print("用户已存在")
    elif bankadd == 3:
        print("数据库已满")


# 获取存钱的账户信息
def cun():
        n = 4
        m = 0
        account = int(input("请输入你的账号："))
        sql = "select * from users where account=%s"
        param = [account]

        date = select(sql, param)
        if len(date) > 0:
            while True:
                password = int(input("请输入您的密码"))
                sal1 = 'select password from users where account=%s'
                param1 = [account]
                date1 = select(sal1, param1, mode='one')[0]
                if password == date1:
                    withdraw_money = int(input("请输入你要取款的金额："))
                    sal2 = 'select money from users where account=%s'
                    param2 = [account]
                    date2 = select(sal2, param2, mode='one')[0]
                    if withdraw_money > date2:
                        print("您的余额不足！余额：", date2)
                        break
                    else:
                        sal3 = 'update users set money =money-%s where account=%s'
                        param3 = [withdraw_money, account]
                        update(sal3, param3)
                        date3=select(sal2,param2,mode='one')[0]
                        print("取钱成功！您的余额为：", date3)
                        break
                else:

                    print("密码不正确!您还有", n - 1, "次机会")
                    m += 1
                    n -= 1
                    if m == 4:
                        print("该账号今日已锁定，请明天再来。")
                        break
        else:
            print("您输入的账号不存在！")
# 获取取钱信息
def qu():
    account = int(input("请输入你的账号："))
    sql = "select * from users where account=%s"
    param = [account]
    dete = select(sql, param)
    if len(dete) > 0:
        money = int(input("请输入你要存的金额："))
        sql1 = 'update users set money=money+%s where account=%s'
        param1 = [money, account]
        update(sql1, param1)
        sql2 = 'select money from users where account=%s'
        param2 = [account]
        date = select(sql2, param2)
        print("存款成功！你的余额为：", date)
    else:
        print("您输入的账号不存在！")
# 账户
def zhuanzhang():
    a=int(input("请输入转钱账户"))
    sql="select password from users where account=%s"
    param=[a]
    date1=select(sql,param)
    b=int(input("请输入收钱账户"))
    sqll = "select * from users where account=%s"
    param1 = [b]
    date= select(sqll, param1)
    if len(date)>0 and len(date1)>0:
            password=int(input("请输入你的密码"))
            date2=select(sql,param,mode='one')[0]

            if password==date2:
                money=int(input("请输入你要转账的钱数"))
                sql3="select money from users where account=%s"
                param3=[a]
                date3=select(sql3,param3)
                print(date3[0][0])
                if date3[0][0]<money:
                    print("你的钱数不足")
                else:
                    sql4 = 'update users set money=money-%s where account=%s'
                    param4 = [money, a]
                    update(sql4, param4)
                    sal6 = 'update users set money=money+%s where account=%s'
                    param6 = [money,b]
                    update(sal6, param6)
                    print("转账成功")
    else:
        print("账户不存在")
def chaxun():
    a=int(input("请输入您要查询的账号："))
    sql="select * from users where account=%s"
    param=[a]
    date=select(sql, param)
    if len(date)>0:
        password=int(input("请输入你的密码"))
        sql1="select password from users where account=%s"
        pram1=[a]
        date1=select(sql1,pram1,mode='one')[0]
        if password==date1:
            sql2="select * from users where account=%s"
            parm2=[a]
            date2=select(sql2,parm2)
        print(date2)
    else:
        print("你输入的不存在")




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




