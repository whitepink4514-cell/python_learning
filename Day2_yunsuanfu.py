#运算符
#算术运算符
# 整除// ， 取余或求模% ， 幂指数**
"""

print("10 + 4 = ",10+4)
print("10 - 4 = ",10-4)
print("10 * 4 = ",10*4)
print("10 / 4 = ",10/4)
print("10 // 4 = ",10//4)
print("10 ** 4 = ",10**4)
"""
#
#算数运算的优先级为 ** --> * / // %  --> + -
#要求输入两个数x和y，分别输出x+y和x-y的结果
"""
x = float(input("请输入x的值"))
y = float(input("请输入y的值"))
print(f"x+y的值为{x+y},x-y的值为{x-y}")
"""
#浮点数运算可能会设计精度损失，二进制是无法准确表示所有小数

#案例1：计算输入的三个整数的平均数
"""
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
print(f"输入的三个数的平均值为：{(num1 + num2 +num3) / 3}")
"""
#案例2：要求输入梯形的上底，下底，高，然后计算梯形的面积

"""
up_length = float(input("请输入梯形的上底长"))
down_length = float(input("请输入梯形的下底长"))
tall_length = float(input("请输入梯形的高"))
print(f"梯形的面积为{(up_length + down_length ) * tall_length / 2}")
"""

#案例3：要求输入圆的半径，然后计算圆的周长和面积（周长：2*pi*r , 面积：pi * r **2）
"""
import math
print(math.pi)
radius = float(input("请输入圆的半径"))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"圆的周长为{perimeter}，圆的面积为{area}")

"""

#身体质量指数BMI的计算（BMI = 体重(kg) / 身高（m）^2）
"""
weight = float(input("输入体重(kg)"))
height = float(input("输入身高(m)"))
BMI = weight / (height**2)
print(f"身体质量指数BMI结果为：{BMI}")

"""


#赋值运算符
#加法赋值运算符 num += 2 等效为 num = num + 2
#减法赋值运算符 num -= 2 等效为 num = num - 2
#乘法赋值运算符 num *= 2 等效为 num = num * 2
#除法赋值运算符 num /= 2 等效为 num = num / 2
#取模赋值运算符 num %= 2 等效为 num = num % 2
#取整除赋值运算符 num //= 2 等效为 num = num // 2
#幂赋值运算符 num **= 2 等效为 num = num ** 2
"""

num = 85

num += 10
print("num += 10后，num = " , num)
num -= 10
print("num -= 10后，num = " , num)
num *= 10
print("num *= 10后，num = " , num)
num /= 10
print("num /= 10后，num = " , num)
num //= 10
print("num //= 10后，num = " , num)
num %= 10
print("num %= 10后，num = " , num)
num **= 10
print("num **= 10后，num = " , num)

"""

#比较运算符，返回的是一个布尔值
# a == b 判断a是否等于b
# a != b 判断a是否不等于b
# a > b 判断a是否大于b
# a < b 判断a是否小于b

#思考1：数学计算中，判断一个数是否为偶数，使用哪个关系运算符呢?
"""

num = int(input("请输入一个数以判断奇偶"))

if num % 2 == 0:
    print("输入的是偶数")
else:
    print("输入的是奇数")

"""
#逻辑运算符
# and 逻辑与（并且）：同时成立才是符合条件的（左右两边都视为True，结果才为True）
# or 逻辑或（或者）：只有一个符合要求即可
# not 逻辑非（取反）：取反操作，True变为False，False变为True
 
#需求1：键盘上录入一个整数，判断这个数字是否在10~20之间
"""
num  = int(input("请输入一个数"))

if num >=10 and num <=20:
    print("这个数是在10~20之间")
else:
    print("这个数不在10~20之间")
"""

"""
num  = int(input("请输入一个数"))

print(f"{num}在10~20之间" , num>=10 and num<=20)
"""

"""
num  = int(input("请输入一个数"))

print(f"{num}在10~20之间" , num<=10 or num>=20)

"""

#流程控制语句：条件判断 ， 模式匹配 ， 循环

#条件判断
# if 要判断的条件：（：代表代码块的开始）
#     条件成立时，要执行对应的操作

#需求：结合前面学习的输入输出以及if条件判断的知识，完成B站登陆功能的实现（正确账号和密码为18888888888/666888）
#input输入的是字符串，下面是两种方法
"""
Account = int(input("请输入账号："))
Passport = int(input("请输入密码"))

if Account == 18888888888 and Passport == 666888:
    print("欢迎登陆")
else:
    print("账号或密码错误")

Account = input("请输入账号：")
Passport = input("请输入密码")

if Account == "18888888888" and Passport == "666888":
    print("欢迎登陆")
else:
    print("登录失败！")
    print("账号或密码错误")

"""

#需求：根据用户输入的年份，判断这一年是闰年还是平年
#整百年份必须能被400整除的才是闰年，非整百年份能被4整除的才是闰年
"""
year = int(input("用户输入年份"))

if year % 100 == 0:
    if year % 400 == 0:
        print("该年是闰年")
    else:
        print("该年是平年")
else:
    if year % 4 == 0:
        print("该年是闰年")
    else:
        print("该年是平年")

        
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")

"""
#需求1：根据用户输入的数字，判断该数字是奇数还是偶数
"""
num = int(input("用户输入数字："))

if num / 2 ==0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")
"""
#if elif else

"""
if 要判断的条件1：
    条件成立时，执行对应的操作1
elif 要判断的条件：
    条件成立时，执行对应的操作2
else：
    条件不成立时，执行的操作3
"""


#需求2：根据用户输入的数字，判断该数字是正数还是负数（考虑0）
"""
num = int(input("请输入数字："))

if num > 0:
    print("该数字是正数")
elif num < 0:
    print("该数字是负数")
else:
    print("该数是0")
"""
#根据输入用户名，密码进行登录系统
#用户名，密码为admin/666888 或 root/547527 或zhagnsan/123456，则输出登录成功
#否则就提示用户名或密码错误
"""
Account = input("账号：")
Passport = input("密码：")

if Account == "admin" and Passport == "666888":
    print("登录成功")
elif Account == "root" and Passport == "547527":
    print("登录成功")
elif Account == "zhangsan" and Passport == "123456":
    print("登录成功")
else:
    print("用户名或密码错误")
"""

#三角形类型判断：根据输入的三个边的边长（正整数），判断是等边三角形，普通三角形还是不能构成三角形
#方法1：
"""
length1 = float(input("第一条边长"))
length2 = float(input("第二条边长"))
length3 = float(input("第三条边长"))

if length1 == length2 == length3:
    print("等边三角形")
elif (length1 + length2 > length3) and (length1 + length3 > length2) and (length3 + length2 > length1):
    print("普通三角形")
else:
    print("不能构成三角形")
"""

#方法2
"""
length1 = float(input("第一条边长"))
length2 = float(input("第二条边长"))
length3 = float(input("第三条边长"))

if (length1 + length2 > length3) and (length1 + length3 > length2) and (length3 + length2 > length1):
    if length1 == length2 and length2 == length3:
        print(f"{length1},{length2},{length3}这三个边构成等边三角形")
    elif length1 == length2 or length2 == length3 or length1 == length3:
        print(f"{length1},{length2},{length3}这三个边构成等腰三角形")
    else:
        print(f"{length1},{length2},{length3}这三个边构成普通三角形")
else:
    print(f"{length1},{length2},{length3}这三个边不构成三角形")

"""

#模式匹配  match...case
#结构模式匹配就是用一个清晰的 模板 去精准的 匹配 数据的结构和内容，匹配成功则执行响应的操作
#工作日程安排
"""
day = input("请输入星期几（1-7）：")
if day == "1":
    print("周一，工作会议日")
elif day == "2":
    print("周二，学习培训日")
elif day == "3":
    print("周三，项目开发日")
elif day == "4":
    print("周四，代码审查日")
elif day == "5":
    print("周五，总结规划日")
elif day == "6" or day == "7":
    print("周末，休息放松")
else:
    print("输入错误")
"""


#其中的|表示或的意思，匹配多个模式中的一个
"""
day = input("请输入星期几（1-7）：")
match day:
    case "1":
        print("周一，工作会议日")
    case "2":
        print("周二，学习培训日")
    case "3":
        print("周三，项目开发日")
    case "4":
        print("周四，代码审查日")
    case "5":
        print("周五，总结规划日")
    case "6" | "7":
        print("周末，休息放松")
    case _:
        print("输入错误")
"""

#实现一个计算器，可以实现+——*/运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算
"""
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
opera = input("请输入运算符(+ — * / ):")

match opera:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:   #if条件成立，才能匹配/
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持!!!")
"""

#请你编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行响应的动作
# 上/w/W 角色向上移动
# 下/s/S 角色向下移动
# 左/a/A 角色向左移动
# 右/d/D 角色向右移动
# 跳/" "(空格) 角色跳跃
# 攻击/j/J 角色发动攻击
# 推出/esc/ESC 角色退出游戏
"""
command = input("请输入指令")

match command:
    case "上" | "w" | "W" :
        print("角色向上移动")
    case "下" | "s" | "S" :
        print("角色向下移动")
    case "左" | "a" | "A" :
        print("角色向左移动")
    case "右" | "d" | "D" :
        print("角色向右移动")
    case "跳" | " " :
        print("角色跳跃")
    case "攻击" | "j" | "J" :
        print("角色攻击")
    case "退出" | "esc" | "ESC" :
        print("角色退出游戏")
    case _:
        print("输入指令错误！！")
"""
