#Rubik's cubik Solver
import random

#cubik=[['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]


def single_move(cube,move):
    cubik=cube
    if move=='u':
        cubik[0][0],cubik[0][1],cubik[0][2],cubik[0][5],cubik[0][8],cubik[0][7],cubik[0][6],cubik[0][3]=cubik[0][6],cubik[0][3],cubik[0][0],cubik[0][1],cubik[0][2],cubik[0][5],cubik[0][8],cubik[0][7]
        cubik[1][0],cubik[1][1],cubik[1][2],cubik[2][0],cubik[2][1],cubik[2][2],cubik[3][0],cubik[3][1],cubik[3][2],cubik[4][0],cubik[4][1],cubik[4][2]=cubik[2][0],cubik[2][1],cubik[2][2],cubik[3][0],cubik[3][1],cubik[3][2],cubik[4][0],cubik[4][1],cubik[4][2],cubik[1][0],cubik[1][1],cubik[1][2]
    elif move=="u'":
        cubik[0][0],cubik[0][1],cubik[0][2],cubik[0][5],cubik[0][8],cubik[0][7],cubik[0][6],cubik[0][3]=cubik[0][2],cubik[0][5],cubik[0][8],cubik[0][7],cubik[0][6],cubik[0][3],cubik[0][0],cubik[0][1]
        cubik[1][0],cubik[1][1],cubik[1][2],cubik[2][0],cubik[2][1],cubik[2][2],cubik[3][0],cubik[3][1],cubik[3][2],cubik[4][0],cubik[4][1],cubik[4][2]=cubik[4][0],cubik[4][1],cubik[4][2],cubik[1][0],cubik[1][1],cubik[1][2],cubik[2][0],cubik[2][1],cubik[2][2],cubik[3][0],cubik[3][1],cubik[3][2]
    elif move=='f':
        cubik[1][0],cubik[1][1],cubik[1][2],cubik[1][5],cubik[1][8],cubik[1][7],cubik[1][6],cubik[1][3]=cubik[1][6],cubik[1][3],cubik[1][0],cubik[1][1],cubik[1][2],cubik[1][5],cubik[1][8],cubik[1][7]
        cubik[0][6],cubik[0][7],cubik[0][8],cubik[2][0],cubik[2][3],cubik[2][6],cubik[5][2],cubik[5][1],cubik[5][0],cubik[4][8],cubik[4][5],cubik[4][2]=cubik[4][8],cubik[4][5],cubik[4][2],cubik[0][6],cubik[0][7],cubik[0][8],cubik[2][0],cubik[2][3],cubik[2][6],cubik[5][2],cubik[5][1],cubik[5][0]
    elif move=="f'":
        cubik[1][0],cubik[1][1],cubik[1][2],cubik[1][5],cubik[1][8],cubik[1][7],cubik[1][6],cubik[1][3]=cubik[1][2],cubik[1][5],cubik[1][8],cubik[1][7],cubik[1][6],cubik[1][3],cubik[1][0],cubik[1][1]
        cubik[0][6],cubik[0][7],cubik[0][8],cubik[2][0],cubik[2][3],cubik[2][6],cubik[5][2],cubik[5][1],cubik[5][0],cubik[4][8],cubik[4][5],cubik[4][2]=cubik[2][0],cubik[2][3],cubik[2][6],cubik[5][2],cubik[5][1],cubik[5][0],cubik[4][8],cubik[4][5],cubik[4][2],cubik[0][6],cubik[0][7],cubik[0][8]
    elif move=='r':
        cubik[2][0],cubik[2][1],cubik[2][2],cubik[2][5],cubik[2][8],cubik[2][7],cubik[2][6],cubik[2][3]=cubik[2][6],cubik[2][3],cubik[2][0],cubik[2][1],cubik[2][2],cubik[2][5],cubik[2][8],cubik[2][7]
        cubik[1][8],cubik[1][5],cubik[1][2],cubik[0][8],cubik[0][5],cubik[0][2],cubik[3][0],cubik[3][3],cubik[3][6],cubik[5][8],cubik[5][5],cubik[5][2]=cubik[5][8],cubik[5][5],cubik[5][2],cubik[1][8],cubik[1][5],cubik[1][2],cubik[0][8],cubik[0][5],cubik[0][2],cubik[3][0],cubik[3][3],cubik[3][6]
    elif move=="r'":
        cubik[2][0],cubik[2][1],cubik[2][2],cubik[2][5],cubik[2][8],cubik[2][7],cubik[2][6],cubik[2][3]=cubik[2][2],cubik[2][5],cubik[2][8],cubik[2][7],cubik[2][6],cubik[2][3],cubik[2][0],cubik[2][1]
        cubik[1][8],cubik[1][5],cubik[1][2],cubik[0][8],cubik[0][5],cubik[0][2],cubik[3][0],cubik[3][3],cubik[3][6],cubik[5][8],cubik[5][5],cubik[5][2]=cubik[0][8],cubik[0][5],cubik[0][2],cubik[3][0],cubik[3][3],cubik[3][6],cubik[5][8],cubik[5][5],cubik[5][2],cubik[1][8],cubik[1][5],cubik[1][2]
    elif move=='l':
        cubik[4][0],cubik[4][1],cubik[4][2],cubik[4][5],cubik[4][8],cubik[4][7],cubik[4][6],cubik[4][3]=cubik[4][6],cubik[4][3],cubik[4][0],cubik[4][1],cubik[4][2],cubik[4][5],cubik[4][8],cubik[4][7]
        cubik[1][6],cubik[1][3],cubik[1][0],cubik[0][6],cubik[0][3],cubik[0][0],cubik[3][2],cubik[3][5],cubik[3][8],cubik[5][6],cubik[5][3],cubik[5][0]=cubik[0][6],cubik[0][3],cubik[0][0],cubik[3][2],cubik[3][5],cubik[3][8],cubik[5][6],cubik[5][3],cubik[5][0],cubik[1][6],cubik[1][3],cubik[1][0]
    elif move=="l'":
        cubik[4][0],cubik[4][1],cubik[4][2],cubik[4][5],cubik[4][8],cubik[4][7],cubik[4][6],cubik[4][3]=cubik[4][2],cubik[4][5],cubik[4][8],cubik[4][7],cubik[4][6],cubik[4][3],cubik[4][0],cubik[4][1]
        cubik[1][6],cubik[1][3],cubik[1][0],cubik[0][6],cubik[0][3],cubik[0][0],cubik[3][2],cubik[3][5],cubik[3][8],cubik[5][6],cubik[5][3],cubik[5][0]=cubik[5][6],cubik[5][3],cubik[5][0],cubik[1][6],cubik[1][3],cubik[1][0],cubik[0][6],cubik[0][3],cubik[0][0],cubik[3][2],cubik[3][5],cubik[3][8]
    elif move=='b':
        cubik[3][0],cubik[3][1],cubik[3][2],cubik[3][5],cubik[3][8],cubik[3][7],cubik[3][6],cubik[3][3]=cubik[3][6],cubik[3][3],cubik[3][0],cubik[3][1],cubik[3][2],cubik[3][5],cubik[3][8],cubik[3][7]
        cubik[0][2],cubik[0][1],cubik[0][0],cubik[4][0],cubik[4][3],cubik[4][6],cubik[5][6],cubik[5][7],cubik[5][8],cubik[2][8],cubik[2][5],cubik[2][2]=cubik[2][8],cubik[2][5],cubik[2][2],cubik[0][2],cubik[0][1],cubik[0][0],cubik[4][0],cubik[4][3],cubik[4][6],cubik[5][6],cubik[5][7],cubik[5][8]
    elif move=="b'":
        cubik[3][0],cubik[3][1],cubik[3][2],cubik[3][5],cubik[3][8],cubik[3][7],cubik[3][6],cubik[3][3]=cubik[3][2],cubik[3][5],cubik[3][8],cubik[3][7],cubik[3][6],cubik[3][3],cubik[3][0],cubik[3][1]
        cubik[0][2],cubik[0][1],cubik[0][0],cubik[4][0],cubik[4][3],cubik[4][6],cubik[5][6],cubik[5][7],cubik[5][8],cubik[2][8],cubik[2][5],cubik[2][2]=cubik[4][0],cubik[4][3],cubik[4][6],cubik[5][6],cubik[5][7],cubik[5][8],cubik[2][8],cubik[2][5],cubik[2][2],cubik[0][2],cubik[0][1],cubik[0][0]
    elif move=='d':
        cubik[5][0],cubik[5][1],cubik[5][2],cubik[5][5],cubik[5][8],cubik[5][7],cubik[5][6],cubik[5][3]=cubik[5][6],cubik[5][3],cubik[5][0],cubik[5][1],cubik[5][2],cubik[5][5],cubik[5][8],cubik[5][7]
        cubik[1][6],cubik[1][7],cubik[1][8],cubik[2][6],cubik[2][7],cubik[2][8],cubik[3][6],cubik[3][7],cubik[3][8],cubik[4][6],cubik[4][7],cubik[4][8]=cubik[4][6],cubik[4][7],cubik[4][8],cubik[1][6],cubik[1][7],cubik[1][8],cubik[2][6],cubik[2][7],cubik[2][8],cubik[3][6],cubik[3][7],cubik[3][8]
    elif move=="d'":
        cubik[5][0],cubik[5][1],cubik[5][2],cubik[5][5],cubik[5][8],cubik[5][7],cubik[5][6],cubik[5][3]=cubik[5][2],cubik[5][5],cubik[5][8],cubik[5][7],cubik[5][6],cubik[5][3],cubik[5][0],cubik[5][1]
        cubik[1][6],cubik[1][7],cubik[1][8],cubik[2][6],cubik[2][7],cubik[2][8],cubik[3][6],cubik[3][7],cubik[3][8],cubik[4][6],cubik[4][7],cubik[4][8]=cubik[2][6],cubik[2][7],cubik[2][8],cubik[3][6],cubik[3][7],cubik[3][8],cubik[4][6],cubik[4][7],cubik[4][8],cubik[1][6],cubik[1][7],cubik[1][8]

def moves(cube,moves):
    cubik=cube
    for move in moves:
        single_move(cubik,move)

def orientation(mov,front,top):
    front=front.lower()
    top=top.lower()
    algo=[]
    key={'u':'u',"u'":"u'",'f':'f',"f'":"f'",'r':'r',"r'":"r'",'l':'l',"l'":"l'",'b':'b',"b'":"b'",'d':'d',"d'":"d'"}
    if front=='w':
        if top=='b':
            key={'u':'u',"u'":"u'",'f':'f',"f'":"f'",'r':'r',"r'":"r'",'l':'l',"l'":"l'",'b':'b',"b'":"b'",'d':'d',"d'":"d'"}
        elif top=='r':
            key={'u':'r',"u'":"r'",'f':'f',"f'":"f'",'r':'d',"r'":"d'",'l':'u',"l'":"u'",'b':'b',"b'":"b'",'d':'l',"d'":"l'"}
        elif top=='g':
            key={'u':'d',"u'":"d'",'f':'f',"f'":"f'",'r':'l',"r'":"l'",'l':'r',"l'":"r'",'b':'b',"b'":"b'",'d':'u',"d'":"u'"}
        elif top=='o':
            key={'u':'l',"u'":"l'",'f':'f',"f'":"f'",'r':'u',"r'":"u'",'l':'d',"l'":"d'",'b':'b',"b'":"b'",'d':'r',"d'":"r'"}
    elif front=='r':
        if top=='b':
            key={'u':'u',"u'":"u'",'f':'r',"f'":"r'",'r':'b',"r'":"b'",'l':'f',"l'":"f'",'b':'l',"b'":"l'",'d':'d',"d'":"d'"}
        elif top=='y':
            key={'u':'b',"u'":"b'",'f':'r',"f'":"r'",'r':'d',"r'":"d'",'l':'u',"l'":"u'",'b':'l',"b'":"l'",'d':'f',"d'":"f'"}
        elif top=='g':
            key={'u':'d',"u'":"d'",'f':'r',"f'":"r'",'r':'f',"r'":"f'",'l':'b',"l'":"b'",'b':'l',"b'":"l'",'d':'u',"d'":"u'"}
        elif top=='w':
            key={'u':'f',"u'":"f'",'f':'r',"f'":"r'",'r':'u',"r'":"u'",'l':'d',"l'":"d'",'b':'l',"b'":"l'",'d':'b',"d'":"b'"}
    elif front=='y':
        if top=='b':
            key={'u':'u',"u'":"u'",'f':'b',"f'":"b'",'r':'l',"r'":"l'",'l':'r',"l'":"r'",'b':'f',"b'":"f'",'d':'d',"d'":"d'"}
        elif top=='o':
            key={'u':'l',"u'":"l'",'f':'b',"f'":"b'",'r':'d',"r'":"d'",'l':'u',"l'":"u'",'b':'f',"b'":"f'",'d':'r',"d'":"r'"}
        elif top=='g':
            key={'u':'d',"u'":"d'",'f':'b',"f'":"b'",'r':'r',"r'":"r'",'l':'l',"l'":"l'",'b':'f',"b'":"f'",'d':'u',"d'":"u'"}
        elif top=='r':
            key={'u':'r',"u'":"r'",'f':'b',"f'":"b'",'r':'u',"r'":"u'",'l':'d',"l'":"d'",'b':'f',"b'":"f'",'d':'l',"d'":"l'"}
    elif front=='o':
        if top=='b':
            key={'u':'u',"u'":"u'",'f':'l',"f'":"l'",'r':'f',"r'":"f'",'l':'b',"l'":"b'",'b':'r',"b'":"r'",'d':'d',"d'":"d'"}
        elif top=='w':
            key={'u':'f',"u'":"f'",'f':'l',"f'":"l'",'r':'d',"r'":"d'",'l':'u',"l'":"u'",'b':'r',"b'":"r'",'d':'b',"d'":"b'"}
        elif top=='g':
            key={'u':'d',"u'":"d'",'f':'l',"f'":"l'",'r':'b',"r'":"b'",'l':'f',"l'":"f'",'b':'r',"b'":"r'",'d':'u',"d'":"u'"}
        elif top=='y':
            key={'u':'b',"u'":"b'",'f':'l',"f'":"l'",'r':'u',"r'":"u'",'l':'d',"l'":"d'",'b':'r',"b'":"r'",'d':'f',"d'":"f'"}
    elif front=='b':
        if top=='r':
            key={'u':'r',"u'":"r'",'f':'u',"f'":"u'",'r':'f',"r'":"f'",'l':'b',"l'":"b'",'b':'d',"b'":"d'",'d':'l',"d'":"l'"}
        elif top=='w':
            key={'u':'f',"u'":"f'",'f':'u',"f'":"u'",'r':'l',"r'":"l'",'l':'r',"l'":"r'",'b':'d',"b'":"d'",'d':'b',"d'":"b'"}
        elif top=='o':
            key={'u':'l',"u'":"l'",'f':'u',"f'":"u'",'r':'b',"r'":"b'",'l':'f',"l'":"f'",'b':'d',"b'":"d'",'d':'r',"d'":"r'"}
        elif top=='y':
            key={'u':'b',"u'":"b'",'f':'u',"f'":"u'",'r':'r',"r'":"r'",'l':'l',"l'":"l'",'b':'d',"b'":"d'",'d':'f',"d'":"f'"}
    elif front=='g':
        if top=='w':
            key={'u':'f',"u'":"f'",'f':'d',"f'":"d'",'r':'r',"r'":"r'",'l':'l',"l'":"l'",'b':'u',"b'":"u'",'d':'b',"d'":"b'"}
        elif top=='r':
            key={'u':'r',"u'":"r'",'f':'d',"f'":"d'",'r':'b',"r'":"b'",'l':'f',"l'":"f'",'b':'u',"b'":"u'",'d':'l',"d'":"l'"}
        elif top=='y':
            key={'u':'b',"u'":"b'",'f':'d',"f'":"d'",'r':'l',"r'":"l'",'l':'r',"l'":"r'",'b':'u',"b'":"u'",'d':'f',"d'":"f'"}
        elif top=='o':
            key={'u':'l',"u'":"l'",'f':'d',"f'":"d'",'r':'f',"r'":"f'",'l':'b',"l'":"b'",'b':'u',"b'":"u'",'d':'r',"d'":"r'"}
    for m in mov:
        algo.append(key[m])
    return algo

def find_edge(c1,c2,cubik):
    edges=[[5,1,1,7],[5,5,2,7],[5,7,3,7],[5,3,4,7],[1,5,2,3],[2,5,3,3],[3,5,4,3],[4,5,1,3],[0,1,3,1],[0,3,4,1],[0,5,2,1],[0,7,1,1]]
    for edge in edges:
        e=[cubik[edge[0]][edge[1]],cubik[edge[2]][edge[3]]]
        if (c1 in e) and (c2 in e):
            break
    if c1!=e[0]:
        edge[0],edge[1],edge[2],edge[3]=edge[2],edge[3],edge[0],edge[1]
    return edge

def find_corner(c1,c2,c3,cubik):
    corners=[[5,0,1,6,4,8],[5,2,1,8,2,6],[5,6,3,8,4,6],[5,8,2,8,3,6],[0,0,3,2,4,0],[0,2,2,2,3,0],[0,6,1,0,4,2],[0,8,1,2,2,0]]
    for corner in corners:
        c=[cubik[corner[0]][corner[1]],cubik[corner[2]][corner[3]],cubik[corner[4]][corner[5]]]
        if (c1 in c) and (c2 in c) and (c3 in c):
            break
    for index in range(3):
        if c1==c[index]:
            c1_l=index
        elif c2==c[index]:
            c2_l=index
        else:
            c3_l=index

    return corner[2*c1_l:2*c1_l+2]+corner[2*c2_l:2*c2_l+2]+corner[2*c3_l:2*c3_l+2]

def first_layer(cube):
    cubik = cube
    solution=[]
    cross_colours={'w':1,'r':2,'y':3,'o':4}
    num_to_colour={1:'w',2:'r',3:'y',4:'o'}
    free_to_move=[1,2,3,4]
    for colour in cross_colours:
        location=find_edge('g',colour,cubik)
        broken_cubik=0
        while (location[2:4]!=[cross_colours[colour],7]):
            semi_sol=[]
            if location[0]==0:
                m=location[2]-cross_colours[colour]
                if abs(m)==3:
                    semi_sol.append({1:"u'",-1:'u'}[m/abs(m)])
                elif abs(m)==1:
                    semi_sol.append({-1:"u'",1:'u'}[m/abs(m)])
                elif abs(m)==2:
                    semi_sol+=['u','u']
                semi_sol+=orientation(['f','f'],colour,'g')
            elif location[0]==5:
                front_turn={1:'w',5:'r',7:'y',3:'o'}
                semi_sol+=orientation(['f','f'],front_turn[location[1]],'g')
            elif location[1]==1:
                not_free=1
                for i in free_to_move:
                    if i==location[0]:
                        not_free=0
                        break
                if not_free:
                    m=free_to_move[0]-location[0]
                    if abs(m)==3:
                        semi_sol+=orientation({1:['u','f',"u'"],-1:["u'",'f','u']}[m/abs(m)],num_to_colour[location[0]],'g')
                    elif abs(m)==1:
                        semi_sol+=orientation({1:["u'",'f','u'],-1:['u','f',"u'"]}[m/abs(m)],num_to_colour[location[0]],'g')
                    else:
                        semi_sol+=orientation(['u','u','f','u','u'],num_to_colour[location[0]],'g')
                else:
                    semi_sol+=orientation(['f'],num_to_colour[location[0]],'g')
            elif location[1]==7:
                semi_sol+=orientation(['f'],num_to_colour[location[0]],'g')
            else:
                not_free=1
                for i in free_to_move:
                    if i==location[2]:
                        not_free=0
                        break
                if not_free:
                    m=free_to_move[0]-location[2]
                    if abs(m)==3:
                        semi_sol+=orientation({1:['u',{3:"f'",5:'f'}[location[1]],"u'"],-1:["u'",{3:"f'",5:'f'}[location[1]],'u']}[m/abs(m)],num_to_colour[location[2]],'g')
                    elif abs(m)==1:
                        semi_sol+=orientation({1:["u'",{3:"f'",5:'f'}[location[1]],'u'],-1:['u',{3:"f'",5:'f'}[location[1]],"u'"]}[m/abs(m)],num_to_colour[location[2]],'g')
                    else:
                        semi_sol+=orientation(['u','u',{3:"f'",5:'f'}[location[1]],'u','u'],num_to_colour[location[2]],'g')
                else:
                    semi_sol+=orientation([{3:"f'",5:'f'}[location[1]]],num_to_colour[location[2]],'g')

            moves(cubik,semi_sol)
            location=find_edge('g',colour,cubik)
            solution+=semi_sol
            broken_cubik+=1
            if broken_cubik>3:
                return 'Broken cubik!!'

        free_to_move.remove(cross_colours[colour])

    corner_pos={'wr':8,'ry':2,'yo':0,'ow':6}
    for corner in corner_pos:
        location=find_corner('g',corner[0],corner[1],cubik)
        broken_cubik=0
        while [location[0],location[2]]!=[5,cross_colours[corner[0]]]:
            semi_sol=[]
            if location[0]==5:
                front_for_r={0:'w',2:'r',6:'o',8:'y'}
                semi_sol+=orientation(["r'","d'",'r','d'],front_for_r[location[1]],'g')
            elif location[0]!=0 and (location[1] in [6,8]):
                if location[1]==8:
                    front=location[0]+1
                    if front==5:
                        front=1
                    front=num_to_colour[front]
                    semi_sol+=orientation(["r'","d'",'r'],front,'g')
                else:
                    front=location[0]-1
                    if front==0:
                        front=4
                    front=num_to_colour[front]
                    semi_sol+=orientation(['l','d',"l'"],front,'g')
            else:
                for i in [0,2,4]:
                    if location[i]==0:
                        loc_on_blue=location[i+1]
                        break
                if loc_on_blue==corner_pos[corner]:
                    if location[0]==0:
                        front_for_algo={0:'o',2:'y',8:'r',6:'w'}
                        semi_sol+=orientation(["r'","d'","d'",'r','d',"r'","d'",'r'],front_for_algo[location[1]],'g')
                    elif location[1]==2:
                        front=location[0]+1
                        if front==5:
                            front=1
                        front=num_to_colour[front]
                        semi_sol+=orientation(["r'","d'",'r'],front,'g')
                    else:
                        front=location[0]-1
                        if front==0:
                            front=4
                        front=num_to_colour[front]
                        semi_sol+=orientation(['l','d',"l'"],front,'g')
                else:
                    sol=[]
                    broken_cubik2=0
                    while loc_on_blue!=corner_pos[corner]:
                        moves(cubik,['u'])
                        sol.append('u')
                        location=find_corner('g',corner[0],corner[1],cubik)
                        for i in [0,2,4]:
                            if location[i]==0:
                                loc_on_blue=location[i+1]
                                break
                        broken_cubik2+=1
                        if broken_cubik2>3:
                            return 'Broken cubik'
                    if len(sol)==3:
                        solution+=["u'"]
                    else:
                        solution+=sol
            moves(cubik,semi_sol)
            solution+=semi_sol
            location=find_corner('g',corner[0],corner[1],cubik)
            broken_cubik+=1
            if broken_cubik>3:
                return 'Broken cubik'
    return solution

def second_layer(cube):
    cubik=cube
    solution=[]
    second_edges=[['w','r'],['w','o'],['y','r'],['y','o']]
    colour_to_num={'w':1,'r':2,'y':3,'o':4,'g':5,'b':0}
    num_to_colour={1:'w',2:'r',3:'y',4:'o',5:'g',0:'b'}
    for edge in second_edges:
        location=find_edge(edge[0],edge[1],cubik)
        broken_cubik=0
        while [location[0],location[2]]!=[colour_to_num[edge[0]],colour_to_num[edge[1]]]:
            semi_sol=[]
            on_top=0
            for i in [0,2]:
                if location[i]==0:
                    on_top=1
                    break
            if on_top:
                if i==0:
                    edge[0],edge[1]=edge[1],edge[0]
                location=find_edge(edge[0],edge[1],cubik)
                sol=[]
                broken_cubik2=0
                while location[0]!=colour_to_num[edge[0]]:
                    moves(cubik,['u'])
                    sol.append('u')
                    location=find_edge(edge[0],edge[1],cubik)
                    broken_cubik2+=1
                    if broken_cubik2>3:
                        return 'Broken cubik'
                if len(sol)==3:
                    solution.append("u'")
                else:
                    solution+=sol
                l_or_r=colour_to_num[edge[1]]-colour_to_num[edge[0]]
                if l_or_r==1 or l_or_r==-3:
                    semi_sol+=orientation(['u', 'r', "u'", "r'", "u'", "f'", 'u', 'f'],edge[0],'b')
                else:
                    semi_sol+=orientation(["u'", "l'", 'u', 'l', 'u', 'f', "u'", "f'"],edge[0],'b')
            else:
                upper_edges=[[0,1,3,1],[0,3,4,1],[0,5,2,1],[0,7,1,1]]
                broke = 1
                for upper_edge in upper_edges:
                    if cubik[upper_edge[0]][upper_edge[1]]=='b' or cubik[upper_edge[2]][upper_edge[3]]=='b':
                        blue_edge=upper_edge[2]
                        broke = 0
                        break
                if broke:
                    return 'Broken cubik'
                for i in [0,2]:
                    if location[i+1]==5:
                        break
                n=blue_edge-location[i]
                if abs(n)==2:
                    semi_sol+=orientation(["u'", 'r', "u'", "r'", "u'", "f'", 'u', 'f'],num_to_colour[location[i]],'b')
                elif abs(n)==1:
                    semi_sol+=orientation([{1:'u',-1:"u'"}[abs(n)/n],'u', 'r', "u'", "r'", "u'", "f'", 'u', 'f'],num_to_colour[location[i]],'b')
                elif abs(n)==3:
                    semi_sol+=orientation([{-1:'u',1:"u'"}[abs(n)/n],'u', 'r', "u'", "r'", "u'", "f'", 'u', 'f'],num_to_colour[location[i]],'b')
                else:
                    semi_sol+=orientation(['u', 'r', "u'", "r'", "u'", "f'", 'u', 'f'],num_to_colour[location[i]],'b')
            moves(cubik,semi_sol)
            solution+=semi_sol
            location=find_edge(edge[0],edge[1],cubik)
            broken_cubik+=1
            if broken_cubik>2:
                return 'Broken cubik'
    return solution

def third_layer(cube):
    cubik=cube
    solution=[]
    cross_loc=[[0,1],[0,5],[0,7],[0,3]]
    blue=[]
    num_to_colour={1:'w',2:'r',3:'y',4:'o'}
    colour_to_num={'w':1,'r':2,'y':3,'o':4}
    num_on_cross=0
    for cross in cross_loc:
        if cubik[cross[0]][cross[1]]=='b':
            num_on_cross+=1
            blue.append(cross)
    broken_cubik=0
    while num_on_cross!=4:
        semi_sol=[]
        if num_on_cross==0:
            semi_sol+=['f','r','u',"r'","u'","f'",'u','u','f','r','u',"r'","u'",'r','u',"r'","u'","f'"]
        elif num_on_cross==2:
            fro={'o':[[0,1],[0,5]],'y':[[0,5],[0,7]],'r':[[0,7],[0,3]],'w':[[0,1],[0,3]]}
            front=0
            for f in fro:
                if fro[f]==blue:
                    front=f
                    break
            if front!=0:
                semi_sol+=orientation(['f','u','r',"u'","r'","f'"],front,'b')
            else:
                for cross in cross_loc:
                    if cross not in blue:
                        break
                faces={1:'y',5:'r',7:'w',3:'o'}
                front=faces[cross[1]]
                semi_sol+=orientation(['f','r','u',"r'","u'","f'"],front,'b')
        moves(cubik,semi_sol)
        solution+=semi_sol
        broken_cubik+=1
        num_on_cross=0
        for cross in cross_loc:
            if cubik[cross[0]][cross[1]]=='b':
                num_on_cross+=1
                blue.append(cross)
        if broken_cubik>1:
            return 'Broken cubik'

    corner_loc=[0,2,8,6]
    blue_corners=[]
    for corner in corner_loc:
        if cubik[0][corner]=='b':
            blue_corners.append(corner)
    broken_cubik=0
    while len(blue_corners)!=4:
        semi_sol=[]
        if len(blue_corners)==0:
            for i in range(1,5):
                if cubik[i][0]=='b' and cubik[i][2]=='b':
                    headlights=i
                    break
            opp={1:3,2:4,3:1,4:2}
            check=opp[headlights]
            if cubik[check][0]=='b':
                check=num_to_colour[check]
                semi_sol+=orientation(['r','u','u',"r'","u'",'r','u',"r'","u'",'r',"u'","r'"],check,'b')
            else:
                check=num_to_colour[check]
                f={'w':'o','r':'w','y':'r','o':'y'}
                semi_sol+=orientation(['r','u','u','r','r',"u'",'r','r',"u'",'r','r','u','u','r'],f[check],'b')
        elif len(blue_corners)==1:
            for i in range(4):
                if corner_loc[i]==blue_corners[0]:
                    break
            if i==0:
                i=3
            else:
                i-=1
            right_colour={0:3,2:2,8:1,6:4}
            if cubik[right_colour[corner_loc[i]]][2]=='b':
                semi_sol+=orientation(['r','u',"r'",'u','r','u','u',"r'"],num_to_colour[right_colour[corner_loc[i]]],'b')
            else:
                f=right_colour[corner_loc[i]]
                if f==1:
                    f=4
                else:
                    f-=1
                f=num_to_colour[f]
                semi_sol+=orientation(["l'","u'",'l',"u'","l'","u'","u'",'l'],f,'b')
        else:
            front=0
            decide={3:[8,6],4:[2,8],1:[0,2],2:[0,6]}
            for d in decide:
                if decide[d]==blue_corners:
                    front=d
                    break
            if front==0:
                for i in range(1,5):
                    if cubik[i][0]=='b':
                        break
                f=num_to_colour[i]
                semi_sol+=orientation(["r'",'f','r',"b'","r'","f'",'r','b'],f,'b')
            elif cubik[front][0]=='b':
                front=num_to_colour[front]
                semi_sol+=orientation(['r','r','d',"r'",'u','u','r',"d'","r'",'u','u',"r'"],front,'b')
            else:
                front=num_to_colour[front]
                f={'w':'o','r':'w','y':'r','o':'y'}
                semi_sol+=orientation(["r'","f'",'l','f','r',"f'","l'",'f'],f[front],'b')
        moves(cubik,semi_sol)
        solution+=semi_sol
        broken_cubik+=1
        blue_corners=[]
        for corner in corner_loc:
            if cubik[0][corner]=='b':
                blue_corners.append(corner)
        if broken_cubik>1:
            return 'Broken cubik'
    n=0
    loc=5
    for i in range(1,5):
        if cubik[i][0]==cubik[i][2]:
            n+=1
            loc=i
        if n==2:
            loc=0
            break
    broken_cubik=0
    while loc!=0 or cubik[1][0]!='w':
        semi_sol=[]
        if loc!=0:
            if loc==5:
                semi_sol+=["r'",'f',"r'",'b','b','r',"f'","r'",'b','b','r','r',"b'", 'r', "b'", 'l', 'l', 'b', "r'", "b'", 'l', 'l', 'b', 'b']
            else:
                opp={1:'y',2:'o',3:'w',4:'r'}
                semi_sol=orientation(["r'",'f',"r'",'b','b','r',"f'","r'",'b','b','r','r'],opp[loc],'b')
        elif cubik[1][0]!='w':
            semi_sol+={'r':["u'"],'y':['u','u'],'o':['u']}[cubik[1][0]]
        moves(cubik,semi_sol)
        solution+=semi_sol
        n=0
        loc=5
        for i in range(1,5):
            if cubik[i][0]==cubik[i][2]:
                n+=1
                loc=i
            if n==2:
                loc=0
                break
        broken_cubik+=1
        if broken_cubik>2:
            return 'Broken cubik'
    n=0
    loc=5
    for i in range(1,5):
        if colour_to_num[cubik[i][1]]==i:
            n+=1
            loc=i
        if n==2:
            loc=0
            break
    broken_cubik=0
    while loc!=0:
        semi_sol=[]
        if loc==5:
            if cubik[1][1]=='y':
                semi_sol+=['r','r','l','l','d','r','r','l','l','d','d','r','r','l','l','d','r','r','l','l','d','d','u','u']
            elif cubik[1][1]=='r':
                semi_sol+=['u', "r'", "u'", 'r', "u'", 'r', 'u', 'r', "u'", "r'", 'u', 'r', 'u', 'r', 'r', "u'", "r'", 'u']
            else:
                semi_sol+=['u', "f'", "u'", 'f', "u'", 'f', 'u', 'f', "u'", "f'", 'u', 'f', 'u', 'f', 'f', "u'", "f'", 'u']
        else:
            check={1:2,2:3,3:4,4:1}
            opp_colour={1:'y',2:'o',3:'w',4:'r'}
            if cubik[check[loc]][1]==opp_colour[check[loc]]:
                semi_sol+=orientation(['r','r','u','f',"b'",'r','r',"f'",'b','u','r','r'],num_to_colour[check[loc]],'b')
            else:
                semi_sol+=orientation(['l','l',"u'","f'",'b','l','l','f',"b'","u'",'l','l'],opp_colour[check[loc]],'b')
        moves(cubik,semi_sol)
        solution+=semi_sol
        broken_cubik+=1
        n=0
        loc=5
        for i in range(1,5):
            if colour_to_num[cubik[i][1]]==i:
                n+=1
                loc=i
            if n==2:
                loc=0
                break
        if broken_cubik>1:
            return 'Broken cubik'

    return solution

def shuffle(cubik):
    move=['f',"f'",'r',"r'",'l',"l'",'u',"u'",'d',"d'",'b',"b'"]
    shuffle_moves=[]
    for i in range(30):
        shuffle_moves.append(random.choice(move))
    moves(cubik,shuffle_moves)

def efficient(sol):
    i=0
    while i<len(sol)-1:
        check=0
        if i<len(sol)-2:
            if sol[i]==sol[i+1] and sol[i+1]==sol[i+2]:
                del sol[i+1]
                del sol[i+1]
                if len(sol[i])==1:
                    sol[i]=sol[i]+"'"
                else:
                    sol[i]=sol[i][0]
                check=1
        if i<len(sol)-1:
            if sol[i][0]==sol[i+1][0] and ((len(sol[i])==1 and len(sol[i+1])==2) or (len(sol[i])==2 and len(sol[i+1])==1)):
                del sol[i]
                del sol[i]
                check=1
        if check!=1:
            i+=1

def test(number):
    for test in range(number):
        solved_cubik=[['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
        cubik=solved_cubik
        shuffle(cubik)
        shuffled_cubik=cubik
        f=first_layer(cubik)
        s=second_layer(cubik)
        t=third_layer(cubik)
        if type(f)!=list:
            print()
            print('First Layer Problem!!')
            print()
            print(shuffled_cubik)
            break
        if type(s)!=list:
            print()
            print('second Layer Problem!!')
            print()
            print(shuffled_cubik)
            break
        if type(t)!=list:
            print()
            print('Third Layer Problem!!')
            print()
            print(shuffled_cubik)
            break
        efficient(f)
        efficient(s)
        efficient(t)
        moves(shuffled_cubik,f+s+t)
        if shuffled_cubik!=solved_cubik:
            print('Efficiency problem')
            break

if __name__ == '__main__':
    cubik=[['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g']]
    
    f=first_layer(cubik)
    s=second_layer(cubik)
    t=third_layer(cubik)
    if type(f)==str or type(s)==str or type(t)==str:
        print('The cubik is broken!')
    else:
        efficient(f)
        efficient(s)
        efficient(t)
       
        print()
        print('First Layer Solution:')
        if len(f)==0:
            print('Already Solved!')
        else:
            for i in range(len(f)):
                if i!=len(f)-1:
                    print(f[i],end=',')
                else:
                    print(f[i])
        print('Second Layer Solution:')
        if len(f)==0:
            print('Already Solved!')
        else:
            for i in range(len(s)):
                if i!=len(s)-1:
                    print(s[i],end=',')
                else:
                    print(s[i])
        print('Third Layer Solution:')
        if len(f)==0:
            print('Already Solved!')
        else:
            for i in range(len(t)):
                if i!=len(t)-1:
                    print(t[i],end=',')
                else:
                    print(t[i])
