import random as rd
for i in range(255):
    COLORS = ["#"+''.join([rd.choice('ABCDEF0123456789') for i in range(6)])]
    print(COLORS)
