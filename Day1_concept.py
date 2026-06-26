# 字面量：程序中，直接书写的固定值（数据）
#数字类型：整数（int），浮点数（float）
#布尔（bool）：表达实际生活中的逻辑，真或者假：True/False
#布尔类型本质上是属于数字类型，属于整型，True=1, False=0
#字符串（str）：由一个或多个字符组成的文本数据，必须使用引号括起来,"人生苦短，我用python"
#空值（None Type）:表示没有值，或者值未知，或者不适用的情况，None
#也可以用 Ctrl/表示#
"""
print(100)  #整数（int）
print(3.14)  #浮点数（float）
print(True)  #布尔(bool)
print("人生苦短，我用python")  #字符串（str）
print(None) #空值
print(type(False))
print(type(None))
print(False+1) # 1
print(True+1) 


"""

#变量：程序中用来存储数据的容器，变量名=变量的值 num=1114.1
#变量名：由字母、数字、下划线组成，不能以数字开头，不能使用Python的关键字，区分大小写
#变量的命名规范：小驼峰命名法（myVariableName），下划线命名法（my_variable_name）
#变量的使用：定义变量后，可以通过变量名来访问和操作存储的数据
#python中的变量是动态类型语言，一个变量是可以存储不同类型的数据的（但是在项目开发过程中，推荐变量只存储一种类型的数据）
"""
num = 1114.1
print(num)
num = 3.14
print(num)
num = "人生苦短，我用python"   
print(num)

"""
"""
num = 1114.1
num = 3.14
print(num)
"""
"""
num = 1114.1 + 1
print(num)
"""
"""
num = True + 1
print(num)
num = True
print(num)

"""
#课程基础播放量为20.7万，每月新增播放量为50万，请输出未来两个月每个月的播放量
##一条语句可以定义多个变量，也可以连续赋值（a , b = 5 , "python"）

"""
base_views, monthly_increase = 207000, 500000
month1_views = base_views + monthly_increase
month2_views = month1_views + monthly_increase
print(f"第一个月的播放量为：{month1_views}")
print(f"第二个月的播放量为：{month2_views}")
"""

# base_views, monthly_increase = 207000, 500000
# print(f"未来一个月的播放总量为：{base_views + monthly_increase}")
#完成如下需求：分别为a = 10, b = 20, 现需要将这两个变量值交换，然后输出到控制台
"""
a , b = 10 , 20
c = a
a = b
b = c
print(a,b)
"""
#现有三个变量，分别为：a = 100, b = 200, c = 300，请将这三个变量的值进行循环交换，即a的值给b，b的值给c，c的值给a，然后输出到控制台
"""
a , b , c = 100 , 200 , 300
temp = a
a = b
b = c
c = temp
print(a,b,c)
"""
#常见数据类型---->isinstance(数据，类型)--->判断数据是否属于某个类型，返回值为布尔值,如果是：True，如果不是：False
# num = -100
# print(isinstance(num,int))

#字符串的三种定义方式：
#双引号，单引号定义
#三引号定义：三引号可以定义多行字符串，且字符串中的换行会被保留

# s3 = """
#   尊敬的客户：
#      感谢选择我的公司的产品
#      我们将会为你竭诚服务

# """
# print(s3)


#单引号定义字符串时，如果字符串中包含单引号，需要使用转义字符\来表示单引号
"""
s1 = 'It\'s a nice day'

print(s1)
"""
#\n表示换行，\t表示制表符（tab键）
"""
s2 = "Hello\n\tWorld"
print(s2)
print("欢迎大家进入到python课程的学习！\n\t大家记得要坚持每天学习哦！")

"""
Example = """
Hello:
    欢迎大家进入python的学习
    大家一起加油
        好吧
"""
print(Example)

"""
print(type("Hello"))    #str类型
print(type(Hello))      #未定义类型
print(type(None))
"""

#字符串的拼接：使用加号（+）运算符可以将多个字符串连接在一起，形成一个新的字符串
# +号可以用来拼接两个字符串，但是无法将非字符串与字符串进行拼接（非字符串类型需要转换为字符串类型）
"""
slogan = "人生苦短，" + "我用python！"
print(slogan) 
s1 = "人生苦短""我用python"           ",OK"
print(slogan,s1)
"""
"""
slogan = "黑马程序员"  "成就IT黑马"
print(slogan)

slogan = "黑马程序员" + "成就IT黑马"
print(slogan)

s1 = "人生苦短"
s2 = "我用python"

print("吉姆·哈特:" + s1 + "," + s2)
print("吉姆·哈特:" , s1 , s2 )
"""
#"大家好，我是涛哥，今年18岁，学习的专业是软件工程，爱好是python、Java"
"""
name = "涛哥"
age = 18
major = "软件工程"
hobby = "python、Java"
print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + major + "，爱好是" + hobby)
"""

#年龄是int类型，无法直接与字符串进行拼接，需要使用str()函数将年龄转换为字符串类型才能进行拼接
#str(int数字)将int类型的数字转换为字符串

#字符串的格式化
#格式化字符串：使用占位符（%s）来表示需要替换的位置，然后使用%运算符将变量的值传递给占位符
#其中%s表示字符串类型，%d表示整数类型，%f表示浮点数类型
"""
s1 = "涛哥"
print("大家好，我是%s，欢迎大家进入python课程的学习" % s1)

name = "涛哥"
age = 18
major = "软件工程"
hobby = "python、Java"
print("大家好，我是%s，今年%d岁，学习的专业是%s，我平时的爱好是%s" % (name , age , major , hobby))

"""
#也可以通过 f"内容{变量/表达式}"的形式来完成快速格式化
"""
name = "涛哥"
age = 18
major = "软件工程"
hobby = "python、Java"
print(f"大家好，我的名字是{name},今年{age}岁，我的专业是{major}，同时我的爱好是{hobby}")


name = input("请输入你的名字")
age = input("请输入您的年龄")
print(f"欢迎您，{name}，您今年{age}岁啦！")
"""

#小智银行卡中有1万元，现在到ATM进行取钱操作，请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额
#因为键盘输入的都是字符串类型，而balance是int类型，不能直接减
"""

balance = 10000
withdraw_amount = float(input("请输入您需要取出的金额："))
settle_amount = float(balance - withdraw_amount)
print(f"取现已完成，您的卡内还剩{settle_amount}元")

print(f"取现已完成，您的卡内还剩{balance - int(withdraw_amount)}元")

"""
#int()其他类型转换为整数类型，bool()其他类型转换为布尔类型，str()其他类型转换为字符串类型，float()其他类型转换为浮点数类型
#根据用户输入的两个数字，计算两个数之和，将其输出到控制台
"""

num1 = int(input("请输入第一个数"))
num2 = int(input("请输入第二个数"))
print(f"输入的两个数之和为{num1 + num2}")

"""

#运算符
# 整除// ， 取余或求模% ， 幂指数**
"""

print("10 + 4 = ",10+4)
print("10 - 4 = ",10-4)
print("10 * 4 = ",10*4)
print("10 / 4 = ",10/4)
print("10 // 4 = ",10//4)
print("10 ** 4 = ",10**4)
"""

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
pi = 3.14
radius = float(input("请输入圆的半径"))
perimeter = 2 * pi * radius
area = pi * radius ** 2
print(f"圆的周长为{perimeter}，圆的面积为{area}")

"""

