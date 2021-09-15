# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random

list = ["许浩","杀子","奥巴马","塞纳","德邦"]
a = int(input("请选择你要惩罚的人"))
for i in list:
 s=list[a-1]
ran=random.randint(1,50)
print(s,"处罚了",ran,"遍")

