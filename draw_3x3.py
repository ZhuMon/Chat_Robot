order = []
def draw(order):
    graph = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]
    for i in range(0, len(order)):
        j = -1
        if order[i][0] == "A":
            j = 0
        elif order[i][0] == "B":
            j = 1
        elif order[i][0] == "C":
            j = 2
        
        #if j == -1:
        #    exit()
        
        k = -1
        if order[i][1] == "1":
            k = 0
        elif order[i][1] == "2":
            k = 1
        elif order[i][1] == "3":
            k = 2

        if i%2 == 0:
            graph[k][j] = "x"
        else:
            graph[k][j] = "o"

    graph_str = ("    A   B   C \n 1 "+graph[0][0]+" | "+graph[0][1]+" | "+graph[0][2]+" \n   ---|---|---\n 2  "+graph[1][0]+" | "+graph[1][1]+" | "+graph[1][2]+" \n   ---|---|---\n 3 "+graph[2][0]+"  | "+graph[2][1]+" | "+graph[2][2]+" ")
    return graph_str

