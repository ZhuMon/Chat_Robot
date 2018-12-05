import sys

num = input("How many? ")

lost_list = []
all_list = []

for i in range(0, int(num)):
    in_data = input()
    in_list = in_data.split('\t');
    all_list.append(in_list)

#print(in_list)

for order in range(0, int(num)):
    opt_num = 0
    opt_done = [0,0,0,0]
    for j in range(0, 4):
        state = ""
        while_bool = True  # only order to break
        if lost_list == []:
            while_bool = False
            for i in range(0, 4):
                if (i == 2 or i == 3) and all_list[order][2*i] != "" and all_list[order][2*i][0] == '(':
                    if all_list[order][8] == "x":
                        state = state + "x"
                    elif all_list[order][8] == "e":
                        state = state + "e"
                else:
                    state = state + all_list[order][2*i]
                if opt_done[i] == 0:
                    opt_done[i] = 1
                    opt_num = 2*i
                    break

        if opt_num == 6 and all_list[order][6] == "":
            break   	

        # if once diff, do next always
        while while_bool == True:
            state = all_list[order][0]
            while_bool = False
                # already has first state
            if all_list[order][0] == lost_list[0]:
                state = state + all_list[order][2]
                opt_num = 2
                #opt_done[1] = 1
            else:
                if opt_done[0] == 1:
                    state = state + all_list[order][2]
                    opt_num = 2
                else:
                    opt_done[0] = 1
                    break

            if all_list[order][2] == lost_list[2] and all_list[order][4] != "" and all_list[order][4][0] == '(':
                state = state + "x"
                opt_num = 4
                opt_done[2] = 1
                break
            elif all_list[order][2] == lost_list[2]:
                state = state + all_list[order][4]
                opt_num = 4
                #opt_done[2] = 1
            
            else:
                if opt_done[1] == 1:
                    if all_list[order][4] != "" and all_list[order][4][0] == '(':
                        state = state + "x"
                        opt_num = 4
                        opt_done[2] = 1
                        break
                    else:
                        state = state + all_list[order][4]
                        opt_num = 4
                        opt_done[2] = 1
                        
                    
                else:
                    opt_done[1] = 1
                    break

            if all_list[order][4] == lost_list[4] and all_list[order][8] == "x" and all_list[order][6] != "" and all_list[order][6][0] == '(':
                state = state + "x"
                opt_num = 6
                opt_done[3] = 1
                break
            elif all_list[order][4] == lost_list[4] and all_list[order][8] == "e" and all_list[order][6] != "" and all_list[order][6][0] == '(':
                state = state + "e"
                opt_num = 6
                opt_done[3] = 1
                break
            elif all_list[order][4] == lost_list[4]:
                state = state + all_list[order][6]
                opt_num = 6
                opt_done[3] = 1
                break
            else:
                # opt_done[2]


                if opt_done[3] == 1:
                    if all_list[order][6] != "" and all_list[order][6][0] == '(':
                        if all_list[order][8] == "x": 
                            state = state + "x"
                        elif all_list[order][8] == "e":
                            state = state + "e"
                        elif all_list[order][8] == "o":
                            state = state + "o"
                    else:
                        state = state + all_list[order][6]
                    opt_num = 6
                else:
                    opt_done[3] = 1
                    break


        s1 = ""
        s2 = ""
        s3 = ""
        s4 = ""
        s5 = ""
        s6 = ""
        s7 = ""
        s8 = ""

        if opt_num >= 0:
        	s1 = all_list[order][0]
        	s2 = all_list[order][1]
        if opt_num >= 2:
        	s3 = all_list[order][2]
        	s4 = all_list[order][3]
        if opt_num >= 4:
        	s5 = all_list[order][4]
        	s6 = all_list[order][5]
        if opt_num >= 6:
        	s7 = all_list[order][6]
        	s8 = all_list[order][7]


        print("    def to_"+state+"(self, event):")
        print("        if event.get(\"message\"):")
        print("            text = event['message']['text']")
        # if (A1, ...) exist
        if all_list[order][opt_num] != "" and all_list[order][opt_num][0] == '(':
            o_block = all_list[order][opt_num].split(',')
            print_tmp = "            if "
            for i in range(0, len(o_block)): #o_block: 選的cell會使user輸
                o_block[i] = o_block[i].replace('(', '')
                o_block[i] = o_block[i].rstrip()
                o_block[i] = o_block[i].lstrip()
                o_block[i] = o_block[i].replace(')', '')

                if i != len(o_block)-1:
                    print_tmp = print_tmp + "text == \"" + o_block[i] + "\" or "
                else:
                    print_tmp = print_tmp + "text == \"" + o_block[i] + "\":"
            print(print_tmp)
        else:
            print("            if text == \""+all_list[order][opt_num]+"\" :")
        print("                return True")
        print("        return False")
        print()
        print("    def on_enter_"+state+"(self, event):")
        print("        sender_id = event['sender']['id']")
        print("        new = event['message']['text']")

        # if 1
        if opt_num == 0:
        	print("        new_image = bind_image([new], sender_id)")
        # elif 3
        elif opt_num == 2:
        	print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", new], sender_id)")
        # elif 5
        elif opt_num == 4:
        	print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", \""+s3+"\", \""+s4+"\", new], sender_id)")
        # elif 7
        elif opt_num == 6:
        	print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", \""+s3+"\", \""+s4+"\", \""+s5+"\", \""+s6+"\", new], sender_id)")
        else:
        	sys.exit()

        print("        responce = send_image_url(sender_id, new_image)")

        if opt_num == 0:
            print("        new_image = bind_image([new, \""+s2+"\"], sender_id)")
            print("        responce = send_image_url(sender_id, new_image)")
        elif opt_num == 2:
            print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", new, \""+s4+"\"], sender_id)")
            print("        responce = send_image_url(sender_id, new_image)")
        # elif 5
        elif opt_num == 4:
            print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", \""+s3+"\", \""+s4+"\", new, \""+s6+"\"], sender_id)")
            print("        responce = send_image_url(sender_id, new_image)")
        # elif 7
        elif opt_num == 6 and all_list[order][7] != "":
            print("        new_image = bind_image([\""+s1+"\", \""+s2+"\", \""+s3+"\", \""+s4+"\", \""+s5+"\", \""+s6+"\", new, \""+s8+"\"], sender_id)")
            print("        responce = send_image_url(sender_id, new_image)")
        

        

        # if lose:
        if (opt_num == 4 and all_list[order][6] == "") or opt_num == 6:    
            if all_list[order][8] == "x":
                print("        responese = send_text_message(sender_id, \"You lose\")")
                print("        self.go_back()")
            # elif 平手：
            elif all_list[order][8] == "e":
                print("        responese = send_text_message(sender_id, \"平手\")")
                print("        self.go_back()")
            # elif win:
            elif all_list[order][8] == "o":
                print("        responese = send_text_message(sender_id, \"You win\")")
                print("        self.go_back()")

        print("\n\n")

        if opt_num == 6 or (opt_num == 4 and all_list[order][6] == ""):
            break
    lost_list = all_list[order]
