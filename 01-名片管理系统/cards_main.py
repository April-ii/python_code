#!/home/sgwf/anaconda3/bin/python


"""
功能:1.新建名片;2.显示全部;3.查询名片　0.退出系统
"""


import cards_tool

while True:

    cards_tool.show_menu()
    # 无限循环的应用场景如下
    action_str = input("请输入希望执行的操作:")
    print("您选择的操作是【%s】" % action_str)
    # 此处不用int转换，原因是如果用户输入的不是字符串，程序会报错

    # TODO 显示功能菜单
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tool.new_card()
        elif action_str == "2":
            cards_tool.show_all()
        elif action_str == "3":
            cards_tool.search_card()
        pass
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")
        break
    else:
        # 这里考虑了用户输入非字符串or超出数字字符范围
        print("您输入的不正确，请重新选择")