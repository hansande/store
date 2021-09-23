# info = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]]

# # money=(500+501+600+700)/4
# # print("平均工资为:",money)
# # age=(56+19+19+45)/4
# # print("平均年龄为:",age)
# name=["刘备","45","男","220","alibaba",500,"30"]
# info.append(name)
# print(info)
# a=0
# b=0
# for i in range(len(info)):
#     if info[i][2]=='男':
#         a+=1
#     elif info[i][2]=='女':
#         b+=1
# print("男生人数为:",a,"女生人数为:",b)

#
# for i in range(len(info)):
#     a= info[i][6]
#
#     print(a)
# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？

# info=[["罗恩", 23 ,35 ,44],["哈利",60, 77 ,68 ,88, 90],["赫敏", 97 ,99 ,89 ,91, 95, 90],["马尔福" ,100, 85 ,90]]
# c=0
# for i in  range(len(info)):
#     for a in  range(1,len(info[i])):
#         c=info[i][a]+c
#     print(info[i][0],c)
#     c=0

# 第三题对购物车系统进行改造：
# （1）	添加登陆功能，登陆后才能进行购物操作。
# （2）	添加结算积分添加功能。
# （3）	登陆成功后系统随机分发一张优惠券（免单券6张，免半券3张，满600减100券50张，满10000减1000券10张，无券）前提是优惠券存在列表中。
#
# shop = [
#     ["劳力士手表",20000],
#     ["迪迦奥特曼",12000],
#     ["喜之郎",6000],
#     ["HW",1200],
#     ["cb",15000],
#     ["辣条",2.5],
#     ["老干妈",13]
# ]
# money = input("请输入您的余额：")
# money = int(money)  # "200000" --> 200000
#
# # 2.2抽奖优惠券
# print("您是否抽取优惠券？抽取请输入a，不抽取请输入b")
# while True:
#     excract=input("请输入您的选择")
#     if excract == "a":
#         import random
#         ran = random.randint(1,30)
#         print(ran)
#         if ran <= 10:
#             print("恭喜您抽到了一张老干妈7折优惠券")
#             break
#         else:
#             print("恭喜您抽中大奖了，您抽到了迪迦奥特曼1折优惠券")
#             break
#         print(ran)
#     elif excract == "b":
#         print("祝您购物愉快")
#         break
#
# # 3.空的购物车
# mycart = []
#
# # 4.买东西
# i = 0
# while i <= 20:
#     # 4.1 展示商品
#     for key, value in enumerate(shop):
#         print(key, value)
#     # 4.2 请输入您想要的商品
#     chose = input("请输入您想要的商品编号：") # "1"
#     # 4.3
#     if chose.isdigit():
#         chose = int(chose)
#         # 4.4 先判断是否存在该商品
#         if chose > 6:
#             print("您输入的商品不存在！别瞎输！")
#         else:
#             # 4.5 判断您的余额是否足够
#             if excract == "a":
#                 if ran <= 10:
#                     money2 = shop[6][1] * 0.7
#                     if money >= money2:
#                         mycart.append(shop[chose])
#                         money = money - money2
#                         print("hhh",money)
#                     else:
#                         print("不够")
#                 if 10 < ran <= 30:
#                     money3 = shop[2][1] * 0.1
#                     if money >= money3:
#                         mycart.append(shop[chose])
#                         money = money - money3
#                         print("你现在的余额为",money)
#                     else:
#                         print("你剩余的钱不够,请及时充值")
#                     # print("ok",money)
#                 # else:
#                 #     money = money - shop[2][1] * 0.1
#                 #     print("okk",money)
#             elif excract == "b":
#                 if money < shop[chose][1]:
#                     print("对不起，穷鬼，您的钱不够！请出门右转！")
#                 else:
#             #     # 4.6 将商品添加到购物车 ，余额减去对应的钱
#                     mycart.append(shop[chose])
#                     money = money - shop[chose][1]
#                     print("恭喜，成功添加购物车！您的余额还剩￥：",money)
#     elif chose == "q" or chose == "Q":
#         print("退出成功！欢迎下次光临！")
#         break
#     else:
#         print("对不起，输入有误，请重新输入！")
#     i = i + 1
#
# # 打印购物小条
# print("以下是您的购物小条，请拿好：")
# for key ,value in  enumerate(mycart):
#     print(key,value)
# print("本次余额还剩：￥",money)
# print("您的本次积分为",len(mycart),"分")
































# # 第五题
# num=int(input('输入一个数：'))
# while num!=0 :
#     print(num%10)
#     num=num//10




#  # 第六题 冒泡排序
# #
# #
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# for i in range(len(a)):
#  j=1
#  while j < (len(a) - i):
#         if a[j-1] > a[j]:
#            a[j-1],a[j]=a[j],a[j-1]
#         j=j+1
#
# print(a)

# a=56
# b=76
# c=0
# c=a
# a=b
# b=c
# print(a,b)



