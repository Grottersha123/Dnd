from functools import reduce
from operator import mul
import matplotlib.pyplot as plt

"""We need to construct the graphics whith max plot"""

def chance_to_attack(att_r,ac,str_):
	y = []
	str_.sort()
	for j in str_:
		y.append(reduce(mul,[round((20+j+i-ac),4)/20 for i in att_r]))
	return str_,y

def chance_to_attack_buff(att_r,ac,str_,buff):
	y = []
	str_.sort()
	for j in str_:
		y.append(reduce(mul,[round((20+j+buff+i-ac)/20,4) for i in att_r if (20+j+buff+i-ac)/20 > 0]))
	str_ = [i+buff for i in str_]
	return str_,y
def chance_to_attack_debuff(att_r,ac,str_,debuff):
	y = []
	str_.sort()
	for j in str_:
		y.append(reduce(mul,[round((20+j+i-ac-debuff)/20,4) for i in att_r if(20+j-debuff+i-ac)/20 > 0]))
	str_ = [i-debuff for i in str_]
	return str_,y

def sub_chances(chan,_chan,st1,st2):
        if _chan[0] > chan[0]:
                t = [_chan[i] - chan[i] for i in range(len(chan))]
                s = [st2[i] - st1[i] for i in range(len(st1))]
        if _chan[0]< chan[1]:
                t = [chan1[i] - _chan[i] for i in range(len(chan))]
                s = [st1[i] - st2[i] for i in range(len(st1))]
        return s,t


def print_graphics(x,y):
        fig = plt.figure()
        m = x.index(max(x))
        mx = max(x)
        my = y[m]
        graph1 = plt.plot(x,y,'ro',x,y)
        scatter1 = plt.scatter(mx+0.1, my,c='green')
        for i in range(len(x)):
                plt.text(x[i]+0.001,y[i]+0.001,str(y[i]))
        plt.show()
def print_graphics_compare(x,y,x1,y1):
        fig = plt.figure()
        #scatter1 = plt.scatter(0.0, 1.0)
        graph1 = plt.plot(x,y,'ro',x,y,'k',x1,y1,'bo',x1,y1,'g')
        
        plt.show()

roll = [7,7,2]
ac = 20
str_ = [-1,3,2,1,5]
b = 2
db = 2
chan1 = chance_to_attack(roll,ac,str_)
chan2 = chance_to_attack_buff(roll,ac,str_,b)
chan3 = chance_to_attack_debuff(roll,ac,str_,db)
chan4 = sub_chances(chan1[1],chan2[1],chan1[0],chan2[0])
chan5 = sub_chances(chan1[1],chan3[1],chan1[0],chan3[0])
print('chance without buff')
print(chance_to_attack(roll,ac,str_))
print_graphics(chan1[0],chan1[1])
print('with buff')
print_graphics(chan2[0],chan2[1])
print(chance_to_attack_buff(roll,ac,str_,b))
#print_graphics_compare(chan1[0],chan1[1],chan2[0],chan2[1])
print('with debuff')
print(chance_to_attack_debuff(roll,ac,str_,db))
print_graphics(chan3[0],chan3[1])
print('substrackt buff - chance')
print('substrackt chance - debuff')
print(sub_chances(chan1[1],chan2[1],chan1[0],chan2[0]))
print(sub_chances(chan1[1],chan3[1],chan1[0],chan3[0]))
print_graphics(chan5[0],chan5[1])
        
