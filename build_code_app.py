import sys

num = input("How many? ")

lost_list = []
all_list = []

machine_states = ""

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



        machine_states = machine_states + "\'"+state+"\', "


        if len(state) == 2: # source = user
            source = "user"
        elif len(state) == 4:
            source = state[0:2]
        elif len(state) == 5 or len(state) == 6:
            source = state[0:4]
        elif len(state) == 7 or len(state) == 8:
            source = state[0:6]

        if state[0:2] == "A1":
            trigger = "a_one"
        elif state[0:2] == "A2":
            trigger = "a_two"
        elif state[0:2] == "A3":
            trigger = "a_three"
        elif state[0:2] == "B1":
            trigger = "b_one"
        elif state[0:2] == "B2":
            trigger = "b_two"
        elif state[0:2] == "B3":
            trigger = "b_three"
        elif state[0:2] == "C1":
            trigger = "c_one"
        elif state[0:2] == "C2":
            trigger = "c_two"
        elif state[0:2] == "C3":
            trigger = "c_three"
            
        transions = '''
        {
            'trigger': \''''+trigger+'''\',
            'source': \''''+source+'''\',
            'dest': \''''+state+'''\',
            'conditions': 'to_'''+state+'''\'
        },'''

        print(transions)
        if opt_num == 6 or(opt_num == 4 and all_list[order][7] == ""):
            break


    lost_list = all_list[order]

print("\n\n"+machine_states)
