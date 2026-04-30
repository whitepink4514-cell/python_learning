#掌握布尔类型用于表示：真和假
#掌握比较运算符用于计算：真和假
#布尔类型的数据，不仅可以通过定义得到，也可以通过比较运算符进行内容比较得到
# ==判断内容是否相等，相等为True,不相等为False
# ！=判断内容是否不相等，不相等为True，相等为False

#定义变量存储布尔类型的数据
"""
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")

num1 = 10
num2 = 20
print(f"10 == 10的结果是：{num1 == num1}")

num1 = 10
num2 = 15
print(f"10 != 15的结果是：{num1 != num2}")

name1 = "itcast"
name2 = "itheima"
print(f"itcase == itheima 的结果是：{name1 == name2}")

num1 = 10
num2 = 5
print(f"10 > 5结果是：{num1 > num2}")
print(f"10 < 5结果是：{num1 < num2}")
print(f"10 >= 5结果是：{num1 >= num2}")
print(f"10 <= 5结果是：{num1 <= num2}")
"""

#if语句的基本格式
"""
if 要判断的条件：（：不能省略）
    条件成立时，要做的事情（前面是4个空格）

age = 30
if age >= 18:
    print("已经成年了")
    print("即将步入大学")
print("时间过得真快")
"""

#例题
"""
print("欢迎来到黑马儿童游乐园，儿童免费，成人收费")
age = input("请输入你的年龄：")
age = int(age)
#age = int(input("请输入你的年龄："))
if age >=18:
    print("您已经成年，游玩需要补票10元")
print("祝您游玩愉快")
"""

#if else
"""
if 条件：
    满足条件要做的事情1
    满足条件要做的事情2
else：
    不满足条件要做的事情1
    不满足条件要做的事情2
"""
#例题1
"""
print("欢迎来到黑马儿童游乐园，儿童免费，成人收费")
age = int(input("请输入你的年龄："))
if age >=18:
    print("您已经成年，游玩需要补票10元")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快")
"""
#例题2
"""
print("欢迎来到黑马动物园")
height = int(input("请输入你的身高（cm）:"))
if height >=120:
    print("您的身高超过120cm，游玩需要购票10元")
else:
    print("您的身高未超过120cm，可以免费游玩")

print("祝您游玩愉快")
"""
#if elif else语句
"""
if 条件1：
    条件1满足应做的事情
    条件1满足应做的事情
elif 条件2：
    条件2满足应做的事情
    条件2满足应做的事情
elif 条件3：
    条件3满足应做的事情
    条件3满足应做的事情
else:
    所有条件都不满足应做的事情

"""
#例题1(Ctrl+/表示注释，再一次表示解除注释)
"""
print("欢迎来到黑马程序员")
height = int(input("请输入您的身高（cm）"))
vip_level = int(input("请输入您的vip等级（1~5）"))
day = int(input("请告诉我今天是几号(1~31)："))
if height < 120:
    print("您的身高低于120cm，可以免费游玩")
elif vip_level > 3:
    print("您的VIP等级大于3，可以免费游玩")
elif day == 1:
    print("今天是1号，可以免费游玩")
else:
    print("不好意思，所有条件都不满足，需购票10元")


print("祝您游玩愉快")

# 依次输入三个，更加合适
print("欢迎来到黑马程序员")
if int(input("请输入您的身高（cm）")) < 120:
    print("您的身高低于120cm，可以免费游玩")
elif int(input("请输入您的vip等级（1~5）")) > 3:
    print("您的VIP等级大于3，可以免费游玩")
elif int(input("请告诉我今天是几号(1~31)：")) == 1:
    print("今天是1号，可以免费游玩")
else:
    print("不好意思，所有条件都不满足，需购票10元")


print("祝您游玩愉快")
"""
#例题2
"""
num = 5
#通过键盘输入获取猜想的数字，通过多次if，elif的组合进行猜想比较、
if int(input("请猜一个数字")) == num:
    print("恭喜第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("Sorry , 猜错了") 
"""

#判断语句的嵌套
"""
if 条件：
    满足条件1，做的事情2
    满足条件1，做的事情2
    if 条件2：
        满足条件2，做的事情1
        满足条件2，做的事情1
第二个if ，属于第一个if内，只有第一个if满足条件，才会执行第二个if

"""
#例题1
"""
print("欢迎来到黑马程序员")
if int(input("请输入你的身高（cm）：")) > 120:
    print("您的身高大于120cm，不可以免费游玩")
    print("不过如果你的vip等级高于3，可以免费游玩")
    if int(input("请告诉我你的VIP等级：")) > 3:
        print("恭喜您，您的VIP等级大于3，可以免费游玩")
    else:
        print("Sorry，您需要购票10元")
else:
    print("欢迎你小朋友，可以免费游玩")
"""
#例题2
"""
# 公司要发礼物，条件是1、必须是大于等于18岁小于30岁的成年人；2、同时入职时间需要大于两年，或者级别大于3才可以领取
age = 20
year = 3
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("您的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标了，可以领取礼物")
        elif level > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标了，但是入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了")
else:
    print("Sorry,未成年不可领取礼物")
"""
#例题3(不会的内容)
# 定义一个数字1~10随机产生，通过三次判断来猜出数字
# 1、数字随机产生，范围1~10
# 2、有3次机会猜测数字，通过三层嵌套判断实现
# 3、每次猜不中会提示大了或者小了
#定义变量num,变量内存储随机数字
"""
import random
num = random.randint(1,10)
guess_num = int(input("输入你要猜测的数字："))

#通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜，第一次就中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("再次输入你要猜测的数字："))
    
    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        
        guess_num = int(input("第三次输入你要猜测的数字："))
        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            if guess_num > num:
                print("你猜测的数字大了")
            else:
                print("你猜测的数字小了")

"""

        
