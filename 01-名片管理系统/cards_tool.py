# 记录所有名片字典
card_list = []


def show_menu():
    interface = [
        "*****************************************",
        "欢迎使用【名片管理系统】V1.0",
        " ",
        "1. 新建名片",
        "2. 显示全部",
        "3. 查询名片",
        " ",
        "0. 退出系统",
        "*****************************************"]
    for info_interface in interface:
        print(info_interface)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    # 提示用户输入信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq:")
    email_str = input("请输入邮箱:")
    # 使用用户输入信息建立一个名片字典
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "email": email_str
    }
    # 将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)
    # 提示用户添加成功
    print("添加%s的名片成功！" % card_dict["name"])


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片用户，如果没有，提示用户返回
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        # return下方的代码不会被执行
        # 如果return后面没有任何内容，表示会返回到调用函数的位置，并且不会返回任何结果
        return

    # 打印表头
    for key in ["姓名", "电话", "QQ", "邮箱"]:
        print(key, end="\t\t")
    print("")
    # 打印分割线
    print("=" * 50)
    # 遍历名片列表依次输出名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    # 提示用户输入要搜索的姓名
    find_name = input("请输入要查找的姓名：")
    # 遍历名片列表，查询，如果没有找到，需要提示用户
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 对查询到的名片进行修改和删除
            deal_card(card_dict)
            break

    else:
        print("抱歉，没有找到%s" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片
    """
    print(find_dict)
    action_str = input("请选择要执行的操作"
                       "[1]修改　[2]删除　[0]上级菜单")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱:")

        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容就返回内容，否则发挥字典中原有的值
    """
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户输入内容进行判断，输入了内容则返回结果
    if len(result_str) > 0:
        return result_str
    # 未输入内容，返回原有的值
    else:
        return dict_value
