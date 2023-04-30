import random
import matplotlib.pyplot as plt

def give_number():
    '''Give a number betweem 1 and 100
    if the number bigger than 51, you win the game
    else you loss the game'''
    num=random.randint(1,100)
    if num<=50:
        return False
    if num>50:
        return True

def fool(assets,wager,total):
    '''Gambling mode based on martingale theory'''
    pre_game='win'
    count=1
    init_wager=wager
    x=[0]
    y=[assets]
    while count<total:
        if pre_game=='win':
            if give_number():
                assets+=wager
                x.append(count)
                y.append(assets)
                pre_game='win'
            else:
                assets-=wager
                x.append(count)
                y.append(assets)
                pre_game='loss'
                if assets<0:
                    break
                else:
                    pass
        elif pre_game=='loss':
            wager=wager*2
            if give_number():
                assets+=wager
                wager=init_wager#bank to intial wager
                x.append(count)
                y.append(assets)
                pre_game=='win'
            else:
                assets-=wager
                x.append(count)
                y.append(assets)
                pre_game='loss'
                if assets<0:
                    break
                else:
                    pass
        count+=1
    plt.plot(x,y)   
    plt.show()
        
for i in range(100):
    fool(10000,1000,100)











































