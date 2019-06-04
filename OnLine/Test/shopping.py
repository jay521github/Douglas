goods = [
    ['iphone6s',  5800],
    ['mac book',  9000],
    ['coffee',      32],
    ['python book', 80],
    ['bicyle',    1500],
]

shopping_car = []
salary = input("Salary:")
if salary.isdigit():
    salary = int(salary)
else:
    print("只能输入整数，请重新输入：")
    salary = input("Salary:")
# 用n, i两个变量接收数据，默认把第1个赋给n，第2个值赋给i
for n, i in enumerate(goods, 1):    # enumerate() 给数出的列表内容前加序号（1表示序号从1开始）
    print(n, ">>>", i)

# 反复提示购买
while True:
    # 提醒用户要购买的商品编号
    choice = input("请输入您要购买商品的编号[退出:Q]:")

    # 判断用户输入的是不是整数
    if choice.isdigit():
        choice = int(choice)
        if (choice > 0) and (choice <= len(goods)):  # 判断用户输入的编码是否超出商品的范围
            # 计算余额
            balance = salary - goods[choice - 1][1]  # balance = 余额
            if balance < 0:
                print('您的余额不足,还剩%s' % salary)
            else:
                # 如果余额充足，将要购买的商品加入到购物车
                print("已加入", goods[choice - 1][0], "到您的购物车，当前余额为：", balance)
                salary = balance
                shopping_car.append(goods[choice - 1])
        else:
            print('编码不存在!')
    # 用户选择退出，打印购买的商品清单，以及剩余的钱
    elif choice == 'Q':
        print("--------您购买了以下商品---------")
        for i in shopping_car:
            print(i)
        print("您的余额为：", balance)
        exit()
    # 如果用户输入的既不是整数又不是Q（退出），则提醒用户重新输入
    else:
        print("请重新输入：")
        choice = input("请输入您要购买商品的编号[退出:Q]:")