# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
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
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]

 # 第一题

# dict = {"k1":"v1","k2":"v2","k3":"v3"}
#
# #
# # for item in dict:
# #
# #     print(item)
# for item in dict.values():
#      print(item)
# dict["k4"] = "v4"
# print(dict)
# 第二题
# 小明去超市购买水果，账单如下
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用
# 用水果名称做key，金额做value，创建一个字典

#  第二题
# info = {'苹果':32.8,'香蕉': 22,'葡萄': 15.5}
# print(info)
# Friuts = {"苹果",12.3,"草莓",4.5,"香蕉",6.3,"葡萄",5.8,"橘子",6.4,"殷桃",15.8}
# info={"小明":{"Friuts":{"苹果":4,"草莓":13,"香蕉":10},"money":170.7},'小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},'money':661}}
#
# print(info)

# 第三题编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：
# def count(*list):
#     dict = {}
#     setL = set(list)
#     for i in range(len(setL)):
#         view = setL.pop()
#         dict[view] = list.count(view)
#     return dict
# print("请输入你要输入的列表：")
# a = list(map(int, input().split()))
# dict = count(*a)
# print(dict)





