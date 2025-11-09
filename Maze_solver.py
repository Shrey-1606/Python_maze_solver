#Converting maze to list
maze = open("maze_map.txt","r")
maze_list=[]
for ls in maze : 
    maze_list.append(ls.strip().split())
maze.close()

#Checking matrix row and col length
row=len(maze_list)
col=len(maze_list[0])
end=row*col

#Creating a function for searching
def search(a): 
    a=str(a)
    #Detecting position of element specified
    for i in maze_list: 
        if a in i: 
            p_x=i.index(a)
            p_y=maze_list.index(i)
    #Adding exceptional cases as well so that we wont have to check boundaries again and again
    north=maze_list[p_y-1][p_x] if p_y > 0 else '*'
    east=maze_list[p_y][p_x+1] if p_x < col-1 else '*'
    south=maze_list[p_y+1][p_x] if p_y < row-1 else '*'
    west=maze_list[p_y][p_x-1] if p_x > 0 else '*'
    return a, north, east, south, west

# Defining some necessary conditions and set  
stuck=False   
goal_reached=False
dead_end=set()
goal_list=[]
dir=""

#Moving function 
def move(a):
    goal=False
    st=False
    global visited
    global dead_end
    global end
    global dir
    a,n,e,s,w=search(a)
    visited.add(a)
    if n != '*' and n not in visited.union(dead_end):
        a = n
    elif e != '*' and e not in visited.union(dead_end): 
        a = e 
    elif s != '*' and s not in visited.union(dead_end): 
        a = s 
    elif w != '*' and w not in visited.union(dead_end): 
        a = w
    else: 
        st=True
        dead_end.add(a)
    goal=True if int(a)==end else False
    return a , st , goal




#Making a bruteforcing loop till the goal is reached
while not goal_reached:
    p = "1"
    #Initializing visited set inside bruteforcing loop but outside inner path creating loop
    visited=set()
    path=[]
    while int(p) != end: 
        #I added visited set so that the maze solver never traces its path back
        #And the visited set is refreshed everytime this loop runs 
        visited.add(p)
        path.append(p)
        p,stuck,goal_reached=move(p)
        if stuck:
            if p == "1":
                print("No more paths available — maze is unsolvable ")
                goal_reached = True
            break
    if goal_reached: 
        break

#Creating a copy of maze_list to a variable maze_copy so that if I amend maze_copy the search function isnt affected
maze_copy=[]
for j2 in maze_list: 
    t_l=[]
    for j3 in j2: 
        t_l.append(j3)
    maze_copy.append(t_l)

#Importing directions by arrows for visually seeing the soln of maze
for i2 in maze_copy: 
    for index_list,ele1 in enumerate(i2): 
        if ele1 in path:    
            _,n_n,n_e,n_s,n_w=search(ele1)
            if path.index(ele1) < len(path)-1:
                pos=path.index(ele1)+1
                if path[pos] == n_n: 
                    i2[index_list]="↑"
                elif path[pos] == n_e: 
                    i2[index_list]="→"
                elif path[pos] == n_s: 
                    i2[index_list]="↓"
                elif path[pos] == n_w: 
                    i2[index_list]="←"

                
#Printing maze soln in a cleaner format       
for line in maze_list: 
    for index,ele in enumerate(line):
        if len(ele) == 1 : 
            line[index]=f"   {ele}"
        elif len(ele) == 2: 
            line[index]=f"  {ele}"
        else: 
            line[index]=f" {ele}"
    print("".join(line))
print(maze_list)