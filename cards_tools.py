card_list = []


def show_menu():
    print("*" * 50)
    print("主人，让我做点什么鸭：")
    print("1.新建名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    print("新建名片")
    print("-" * 50)
    name_str = input("输入姓名：")
    phone_str = input("输入手机号：")
    qq_str = input("输入QQ：")
    email_str = input("输入邮箱：")

    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    card_list.append(card_dict)
    print("我记下%s咯！" % name_str)


def show_all():
    print("显示全部名片")
    print("-" * 50)
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %
              (card_dict["name"],
               card_dict["phone"],
               card_dict["qq"],
               card_dict["email"]))


def search_card():
    print("找寻名片")
    print("-" * 50)
