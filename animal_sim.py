import numpy as np 
import random as ran



L1=["black","fat","slow"]
L2=["white","skinny","fast"]
L3=["black","skinny","fast"]
L4=["brown","paralized","paralized"]
L5=["white","skinny","super fast"]
L6=["black","paralized"]



D1 = {
    0:  L3,
    1:  L1,
    2:  L2,
    3:  L4,
    4:  L5,
    5:  L6,
    }

user_in = input("How many animals")



class Animals():
    def __init__(species,):
        species.caleb = []
        for i in range(int(user_in)):
            species.x = ran.randint(0,5)
            species.trait_list = D1.get(species.x)
            species.caleb.append(species.trait_list)
            
        
class Communtiy():
    def __init__(self):
        self.community_list = []



individual = Animals().caleb
eco = Communtiy()

for i in range(int(user_in)):
    eco.community_list.append(individual[i])

final_community =  eco.community_list
print(final_community)
# print(final_community[2])






try:
    with open("Community.txt",mode="w")as Comm:
        Comm.write(str(final_community))
        Comm.close()
except FileExistsError:
    with open("Community.txt",mode="r+")as Comm:
        Comm.truncate(0)
        Comm.write(str(final_community))
        Comm.close()

