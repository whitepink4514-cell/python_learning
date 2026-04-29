"""
#字符串在python中有多种定义形式
#单引号定义法：
name1 = '你好，世界'
print(name1)
print(type(name1))

#双引号定义法
name2 = "你好，世界"
print(name2)
print(type(name2))

#三引号定义法,写法和多行注释一样
name3 = ""你好,世界""
print(name3)
print(type(name3))
"""

"""
#如果想要定义的字符串本身是包括：单引号，双引号自身如何写
#在字符串内包含双引号
name4 = '"你好，世界"'
print(name4)
print(type(name4)) 
#在字符串内包含单引号
name5 = "'你好，世界'"
print(type(name5),name5)
"""

"""
#使用转义字符\
name6 = "\"你好，世界\""
print(type(name6) , name6)
name7 = '\'你好，世界\''
print(type(name7) , name7)
"""

"""
#字符串的拼接
#字符串字面量之间的拼接
print("你好，" + "世界")

#字符串字面量和字符串变量的拼接
name = "你好，世界"
address = "南京市"
tel = str(1234567890)
print("我是：" + name +"，我的地址是：" + address + "我的电话是：" + tel)
"""

"""
#字符串的格式化
name = "黑马程序员"
message = "学IT就来%s" % name
print(message)
# %s中 % 表示：我要占位 ， s表示将变量变成字符串放入占位的位置

"""

"""
class_num = 57
avg_salary = 16781
message = "python大数据学科，北京%s期，毕业平均工资：%s" %(class_num,avg_salary)
print(message)
"""

"""
name = "黑马程序员"
message = "学IT就来:%s" %name
print(message)
"""

"""
#%d:将内容转换为整数，放入占位位置
#%s:将内容转换为字符串，放入占位位置
#%f:将内容转换为浮点数，放入占位位置
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "%s，我成立于：%d，我今天的股价是：%f" % (name , set_up_year , stock_price)
print(message)
"""

"""
#格式化的精度问题
# %5.2f:表示将宽度控制为5，将小数点精度设置为2
# %.2f:表示不限制宽度，只设置小数点精度为2，如：11.345设置%.2f后为11.35（四舍五入）
num1 = 11
num2 = 11.345
print("数字11宽度限制5,结果是：%5d" % num1)
print("数字11宽度限制1,结果是：%1d" % num1)
print("数字11.345宽度限制7,小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制,小数精度2，结果是：%.2f" % num2)
"""

"""
#快速格式化的方式
#语法：f"内容{变量}"的格式来快速格式化，不限类型，不管精度
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"{name}成立于{set_up_year},当今股价为{stock_price}")
#适合对精度没有要求的
"""

#掌握对表达式进行字符串格式化
#表达式：一条具有明确执行结果的代码语句、
"""
print("1 * 1 的结果是：%d" % (1*1))
print(f"1 * 1 的结果是：{1*1}")
print("字符串在python中的类型是:%s" % type('字符串')) 
"""

#练习：公司：传智播客，股票代码：003032，当前股价：19.99，每日增长系数：1.2，经过7天的增长后，股价达到了71.63
"""
name = "传智播客"
stock_code = "003032"
stock_price = 19.99
stockprice_daily_growth_factor = 1.2
growth_days = 7
stock_new_price = 19.99 * 1.2 ** 7
finally_stock_price = stock_price * stockprice_daily_growth_factor ** growth_days 
print(f"我是{name},我的股票代码为{stock_code},目前我的股价为{stock_price},在增长了{growth_days}天后，股价达到了{finally_stock_price}")
print("我是%s，我的股票代码为%s,目前我的股价为%.2f,在增长了%d天后，我的股价将要来到%.2f" % (name , stock_code , stock_price , growth_days , finally_stock_price))

"""
#input语句
"""
print("请告诉我你是谁：")
name = input()
print("我知道了，你是%s" % name)

"""
#name = input("请告诉我你是谁")
#print("我知道了，你是%s" % name)

#输入数字类型
num = input("请告诉我你的银行卡密码是：")
#int_num = int(num)
#print("你的银行卡密码是：" , type(int_num))
print("你的银行卡密码是：%s" % num)




