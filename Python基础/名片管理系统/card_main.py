import card_tools
while True:

    # 显示功能菜单
    card_tools.show_menu()
  
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    if action_str in ["1","2","3"]:
        if action_str == "1":
            card_tools.new_card()
        elif action_str == "2":
            card_tools.show_all()
        elif action_str == "3":
            card_tools.search_card()
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】！")
        break
    else :
        print("没有这样的操作，请重新选择！")