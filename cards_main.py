import cards_tools
while True:
    cards_tools.show_menu()
    action_str = input("请下指令，主人\n")
    print("你的选项是 [%s]" % action_str)
    if action_str in ["1","2","3"]:
        pass
    elif action_str == "0":
        break
    else:
        print("还不会鸭，请多调教")
