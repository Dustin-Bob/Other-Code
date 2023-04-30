import random
import matplotlib.pyplot as plt

''''A function that take n random steps'''
def walk(n):      
    x,y=0,0
    pl_x=[0]
    pl_y=[0]
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(1,0),(-1,0),(0,-1)])#up,right,left,down
        x+=dx
        y+=dy
        pl_x.append(x)
        pl_y.append(y)
        plt.plot(pl_x,pl_y)
    plt.show()
    return (x,y)

people=50
wk=100
conute=0

for i in range(people):
    (x,y)=walk(wk)
    if abs(int(x))**2+abs(int(y))**2>=50:#The Manhattan distance
        conute+=1
    else:
        pass
    print(x,y)
    plt.plot(x,y)
    plt.show()


print('The proportion of people out of distance:'+str(conute/people))















































