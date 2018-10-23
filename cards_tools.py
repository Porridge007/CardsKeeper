import pickle,os
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
    if card_list == []:
        print("还没有名片哟，告诉我几个叭～")
        return
    else:
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
    search_name = input("查谁咧？")
    for card_dict in card_list:
        if caOBrd_dict["name"] == search_name:
            for name in ["姓名", "电话", "QQ", "邮箱"]:
                print(name, end="\t\t")
            print("")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" %
                  (card_dict["name"],
                   card_dict["phone"],
                   card_dict["qq"],
                   card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("母鸡呀！")


def deal_card(found_dict):
    """
    处理查找到的名片
    :param found_dict:传递找到的字典
    :return:
    """
    action_str = input("我做啥咧 "
                       "[1]修改 [2]删除 [0]返回")
    if action_str == "1":
        found_dict["name"] = input_card_info(found_dict["name"], "姓名[回车不修改]：")
        found_dict["phone"] = input_card_info(found_dict["phone"], "手机号[回车不修改]：")
        found_dict["qq"] = input_card_info(found_dict["qq"], "QQ[回车不修改]:")
        found_dict["email"] = input_card_info(found_dict["email"], "邮箱[回车不修改]:")
        print("修改完成")
    elif action_str == "2":
        card_list.remove(found_dict)
        print("吼，木有了")
    else:
        return


def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value:字典原有值 
    :param tip_message: 输入提示文字
    :return: 如果用户输入了内容，则返回内容;否则返回原有值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

def load_data():
    global card_list
    if "data" in os.listdir("bin"):
        with open("bin/data","rb") as f:
             card_list = pickle.load(f)

def save_data():
    with open("bin/data","wb") as f:
        pickle.dump(card_list,f)

