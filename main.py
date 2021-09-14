# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
# 猜字游戏
# 需求：
# 1、猜的数字是系统产生的，不是自己定义的
# 2、键盘输入的   操作完填入：input（“提示”）
# 3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
# 4、循环			操作完填入：while 条件循环
#任务  判断如果你输入的数字大于随机生成的数字那么给一个提示你猜大了
#                      小于                         小了
#起始资充钱 1000  （账户原有资金+刚充值的资金）10%  2000 20%   每猜一次-500一直执行
#游戏开始按1   退出游戏Q
#资金为0 锁死系统
#5次猜对，5次机会用光了就退出
import  random #快速生成随机数模块、包裹。
ran=random.randint(0,99)#范围
#
a=0
print("")
# 点1开始游戏
s=int(input("点击1进入游戏"))
# 当前余额的显示
print("你的余额为",a)
a=int(input("请输入要充值的金额"))
print("你的余额为",a)
a=int(a)

i=0
while i<5:

    num=int(input("请输入你要输的数字"))
    i=i+1

    if num>ran:
        a=a-5001
        print("你大了,剩余次数为:",5-i,"次","当前余额为",a)
    elif num<ran:
        a = a - 500
        print("你小了,剩余次数为:",5-i,"次","当前余额为",a)
    else:
        a=a+3000
        print("恭喜你答对了")
        break











