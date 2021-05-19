import cv2
import numpy as np
import time
from solution import *
import tkinter as tk
import rubiks_cube_3d as cube_3d



time.sleep(1)
font = cv2.FONT_HERSHEY_SIMPLEX  

state=  {
            'u':['w','w','w','w','w','w','w','w','w',],
            'r':['w','w','w','w','w','w','w','w','w',],
            'f':['w','w','w','w','w','w','w','w','w',],
            'd':['w','w','w','w','w','w','w','w','w',],
            'l':['w','w','w','w','w','w','w','w','w',],
            'b':['w','w','w','w','w','w','w','w','w',]
        }

sign_conv={
            'g' : 'F',
            'w' : 'D',
            'b' : 'B',
            'r' : 'R',
            'o' : 'L',
            'y' : 'U'
          }

color = {
        'r'    : (0,0,255),
        'o' : (0,165,255),
        'b'   : (255,0,0),
        'g'  : (0,255,0),
        'w'  : (255,255,255),
        'y' : (0,255,255)
        }
        

blocks = {
        'main': [
            [200, 120], [300, 120], [400, 120],
            [200, 220], [300, 220], [400, 220],
            [200, 320], [300, 320], [400, 320]
        ],
        'current': [
            [20, 20], [54, 20], [88, 20],
            [20, 54], [54, 54], [88, 54],
            [20, 88], [54, 88], [88, 88]
        ],
        'preview': [
            [20, 130], [54, 130], [88, 130],
            [20, 164], [54, 164], [88, 164],
            [20, 198], [54, 198], [88, 198]
        ],
        'l': [
            [50, 280], [94, 280], [138, 280],
            [50, 324], [94, 324], [138, 324],
            [50, 368], [94, 368], [138, 368]
        ],
        'f': [
            [188, 280], [232, 280], [276, 280],
            [188, 324], [232, 324], [276, 324],
            [188, 368], [232, 368], [276, 368]
        ],
        'r': [
            [326, 280], [370, 280], [414, 280],
            [326, 324], [370, 324], [414, 324],
            [326, 368], [370, 368], [414, 368]
        ],
        'u': [
            [188, 128], [232, 128], [276, 128],
            [188, 172], [232, 172], [276, 172],
            [188, 216], [232, 216], [276, 216]
        ],
        'd': [
            [188, 434], [232, 434], [276, 434],
            [188, 478], [232, 478], [276, 478],
            [188, 522], [232, 522], [276, 522]
        ], 
        'b': [
            [464, 280], [508, 280], [552, 280],
            [464, 324], [508, 324], [552, 324],
            [464, 368], [508, 368], [552, 368]
        ],
           }


colorTexts=  {
            'u':[['U',242, 202],['W',(255,255,0),263,210]],
            'r':[['R',380, 354],['R',(0,0,255),400,355]],
            'f':[['F',242, 354],['B',(255,0,0),263,355]],
            'd':[['D',242, 508],['Y',(0,250,250),262,515]],
            'l':[['L',104,354],['O',(0,165,255),120,355]],
            'b':[['B',518, 354],['G',(0,255,0),540,355]],
        }

check_state=[]
solution=[]


cap=cv2.VideoCapture(0)
cv2.namedWindow('Live Camera')

def rotate(side):
    main=state[side]
    f=state['f']
    l=state['l']
    r=state['r']
    u=state['u']
    d=state['d']
    b=state['b']
    
    if side=='f':
        l[2],l[5],l[8],u[6],u[7],u[8],r[0],r[3],r[6],d[0],d[1],d[2]=d[0],d[1],d[2],l[8],l[5],l[2],u[6],u[7],u[8],r[6],r[3],r[0] 
    elif side=='u':
        l[0],l[1],l[2],b[0],b[1],b[2],r[0],r[1],r[2],f[0],f[1],f[2]=f[0],f[1],f[2],l[0],l[1],l[2],b[0],b[1],b[2],r[0],r[1],r[2]
    elif side=='d':
        l[6],l[7],l[8],b[6],b[7],b[8],r[6],r[7],r[8],f[6],f[7],f[8]=b[6],b[7],b[8],r[6],r[7],r[8],f[6],f[7],f[8],l[6],l[7],l[8]
    elif side=='b':
        l[0],l[3],l[6],u[0],u[1],u[2],r[2],r[5],r[8],d[6],d[7],d[8]=u[2],u[1],u[0],r[2],r[5],r[8],d[8],d[7],d[6],l[0],l[3],l[6] 
    elif side=='l':
        f[0],f[3],f[6],d[0],d[3],d[6],b[2],b[5],b[8],u[0],u[3],u[6]=u[0],u[3],u[6],f[0],f[3],f[6],d[6],d[3],d[0],b[8],b[5],b[2]
    elif side=='r':
        f[2],f[5],f[8],d[2],d[5],d[8],b[0],b[3],b[6],u[2],u[5],u[8]=d[2],d[5],d[8],b[6],b[3],b[0],u[8],u[5],u[2],f[2],f[5],f[8]

    main[0],main[1],main[2],main[3],main[4],main[5],main[6],main[7],main[8]=main[6],main[3],main[0],main[7],main[4],main[1],main[8],main[5],main[2]

def revrotate(side):
    main=state[side]
    f=state['f']
    l=state['l']
    r=state['r']
    u=state['u']
    d=state['d']
    b=state['b']
    
    if side=='f':
        l[2],l[5],l[8],u[6],u[7],u[8],r[0],r[3],r[6],d[0],d[1],d[2]=u[8],u[7],u[6],r[0],r[3],r[6],d[2],d[1],d[0],l[2],l[5],l[8]
    elif side=='u':
        l[0],l[1],l[2],b[0],b[1],b[2],r[0],r[1],r[2],f[0],f[1],f[2]=b[0],b[1],b[2],r[0],r[1],r[2],f[0],f[1],f[2],l[0],l[1],l[2]
    elif side=='d':
        l[6],l[7],l[8],b[6],b[7],b[8],r[6],r[7],r[8],f[6],f[7],f[8]=f[6],f[7],f[8],l[6],l[7],l[8],b[6],b[7],b[8],r[6],r[7],r[8]
    elif side=='b':
        l[0],l[3],l[6],u[0],u[1],u[2],r[2],r[5],r[8],d[6],d[7],d[8]=d[6],d[7],d[8],l[6],l[3],l[0],u[0],u[1],u[2],r[8],r[5],r[2] 
    elif side=='l':
        f[0],f[3],f[6],d[0],d[3],d[6],b[2],b[5],b[8],u[0],u[3],u[6]=d[0],d[3],d[6],b[8],b[5],b[2],u[0],u[3],u[6],f[0],f[3],f[6]
    elif side=='r':
        f[2],f[5],f[8],d[2],d[5],d[8],b[0],b[3],b[6],u[2],u[5],u[8]=u[2],u[5],u[8],f[2],f[5],f[8],d[8],d[5],d[2],b[6],b[3],b[0]

    main[0],main[1],main[2],main[3],main[4],main[5],main[6],main[7],main[8]=main[2],main[5],main[8],main[1],main[4],main[7],main[0],main[3],main[6]


def solve(cube):
    rubiks_cube=cube_3d.rubiks_cube
    f=first_layer(cube)
    #print("after f ",orgcube)
    s=second_layer(cube)
    #print("after s",orgcube)
    t=third_layer(cube)
    #print("after t",orgcube)
    efficient(f)
    #print("after ef ",orgcube)
    efficient(s)
    #print("after es ",orgcube)
    efficient(t)
    print("after et",cube2)
    cube_sol = f+s+t
    root = tk.Tk()
    root.geometry("500x500")
    canvas = tk.Canvas(root, height = 400, width = 400)
    canvas.pack()
    #print("after all ",orgcube)
    cube_3d.three_d_cube_moves(rubiks_cube,cube2,0.5,cube_sol,canvas)
    #root.mainloop()

    
    
def color_detect(h,s,v):
    #print(h,s,v)
    if h <7 and s>=100 and v>127 and v<190 or (h>165 and h<180)  :
        return 'r'
    elif h>=7 and h <=20 and s>=100:
        return 'o'
    elif h>=30 and h <= 60 and s>100:
        return 'y'
    elif h>=60 and h<=90 and s > 100 :
        return 'g'
    elif h>105 and h <= 180 and s>120 and v>75:
        return 'b'
    elif h <= 100 and s<10 and v<150:
        return 'w'

    return 'w'

def draw_stickers(frame,stickers,name):
        for x,y in stickers[name]:
            cv2.rectangle(frame, (x,y), (x+30, y+30), (255,255,255), 2)

def draw_preview_stickers(frame,stickers):
        stick=['f','b','l','r','u','d']
        for name in stick:
            for x,y in stickers[name]:
                cv2.rectangle(frame, (x,y), (x+40, y+40), (255,255,255), 2)

def texton_preview_stickers(frame,stickers):
        stick=['f','b','l','r','u','d']
        for name in stick:
            for x,y in stickers[name]:
                sym,x1,y1=colorTexts[name][0][0],colorTexts[name][0][1],colorTexts[name][0][2]
                cv2.putText(preview, sym, (x1,y1), font,1,(0, 0, 0), 1, cv2.LINE_AA)  
                sym,col,x1,y1=colorTexts[name][1][0],colorTexts[name][1][1],colorTexts[name][1][2],colorTexts[name][1][3]             
                cv2.putText(preview, sym, (x1,y1), font,0.5,col, 1, cv2.LINE_AA)  

def fill_stickers(frame,stickers,sides):    
    for side,colors in sides.items():
        num=0
        for x,y in stickers[side]:
            cv2.rectangle(frame,(x,y),(x+40,y+40),color[colors[num]],-1)
            num+=1

def process(operation):
    replace={
                "F":[rotate,'f'],
                "F2":[rotate,'f','f'],
                "F'":[revrotate,'f'],
                "U":[rotate,'u'],
                "U2":[rotate,'u','u'],
                "U'":[revrotate,'u'],
                "L":[rotate,'l'],
                "L2":[rotate,'l','l'],
                "L'":[revrotate,'l'],
                "R":[rotate,'r'],
                "R2":[rotate,'r','r'],
                "R'":[revrotate,'r'],
                "D":[rotate,'d'],
                "D2":[rotate,'d','d'],
                "D'":[revrotate,'d'],
                "B":[rotate,'b'],
                "B2":[rotate,'b','b'],
                "B'":[revrotate,'b']           
    }    
    a=0
    for i in operation:
        for j in range(len(replace[i])-1):
            replace[i][0](replace[i][j+1])
        cv2.putText(preview, i, (700,a+50), font,1,(0,255,0), 1, cv2.LINE_AA)  
        fill_stickers(preview,blocks,state)
        solution.append(preview)
        cv2.imshow('solution',preview)
        cv2.waitKey()
        cv2.putText(preview, i, (700,50), font,1,(0,0,0), 1, cv2.LINE_AA)  
        
if __name__=='__main__':
    preview = np.zeros((700,800,3), np.uint8)

    while True:
        hsv=[]
        cube2=[]
        current_state=[]
        ret,img=cap.read()
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = np.zeros(frame.shape, dtype=np.uint8)   

        draw_stickers(img,blocks,'main')
        draw_stickers(img,blocks,'current')
        draw_preview_stickers(preview,blocks)
        fill_stickers(preview,blocks,state)
        texton_preview_stickers(preview,blocks)

        for i in range(9):
            hsv.append(frame[blocks['main'][i][1]+10][blocks['main'][i][0]+10])
        
        a=0
        for x,y in blocks['current']:
            color_name=color_detect(hsv[a][0],hsv[a][1],hsv[a][2])
            cv2.rectangle(img,(x,y),(x+30,y+30),color[color_name],-1)
            a+=1
            current_state.append(color_name)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        elif k ==ord('w'):
            state['u']=current_state
            check_state.append('u')
        elif k ==ord('d'):
            check_state.append('r')
            state['r']=current_state
        elif k ==ord('a'):
            check_state.append('l')
            state['l']=current_state
        elif k ==ord('s'):
            check_state.append('d')
            state['d']=current_state       
        elif k ==ord('f'):
            check_state.append('f')
            state['f']=current_state       
        elif k ==ord('b'):
            check_state.append('b')
            state['b']=current_state       
        elif k == ord('l'): 
            f=state['f']
            b=state['b']
            d=state['d']
            r=state['r']
            l=state['l']
            u=state['u']
            
            cube2.append(f)
            cube2.append(u)
            cube2.append(r)
            cube2.append(d)
            cube2.append(l)
            cube2.append(b)
            print(cube2)
        elif k == ord('m'):    
            if len(set(check_state))==6:
                f=state['f']
                b=state['b']
                d=state['d']
                r=state['r']
                l=state['l']
                u=state['u']
                cube= []
                cube.append(f)
                cube.append(u)
                cube.append(r)
                cube.append(d)
                cube.append(l)
                cube.append(b)
                
                try:
                    solved=solve(cube)
                    #if solved:
                        #operation=solved.split(' ')
                        #process(operation)
                except:
                    print("error in side detection ,you may do not follow sequence or some color not detected well.Try again")
            else:
                print("all side are not scanned check other window for finding which l to be scanned?")
                print("l to scan:",6-len(set(check_state)))
        cv2.imshow('Preview',preview)
        cv2.imshow('Live Camera',img[0:500,0:500])

    cv2.destroyAllWindows()