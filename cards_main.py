#! /usr/bin/python
import cards_tools

while True:
    cards_tools.show_menu()
    action_str = input("请下指令，主人\n")
    print("你的选项是 [%s]" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tools.new_card()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()
    elif action_str == "0":
        print("寨见了哟～主人sama")
        break
    else:
        print("还不会鸭，请多调教")
