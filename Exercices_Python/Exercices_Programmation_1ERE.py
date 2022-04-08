from audioop import reverse
import random

def random_list_V1():
    L1, L2, nb = [] , [], 1
    for i in range(50):
        while nb % 5 != 0:
            nb = random.randint(0, 1000)
        L1.append(nb)
        nb = 1
    for i in L1:
        if i % 3 == 0:
            L2.append(i)    
    return L1, L2

def random_list_V2():
    L1, L2, nb = [] , [], 1
    for i in range(50):
        while nb % 5 != 0:
            nb = random.randint(0, 1000)
        L1.append(nb)
        nb = 1
    for i in L1:
        if i % 3 == 0:
            L2.append(i)
    L1.sort()
    L2.sort(reverse=True) 
    return L1, L2

def random_list_V3():
    L1, L2, nb = [] , [], 1
    for i in range(50):
        while nb % 5 != 0 and not nb in L1:
            nb = random.randint(0, 1000)
        L1.append(nb)
        nb = 1
    for i in L1:
        if i % 3 == 0:
            L2.append(i)    
    L1.sort()
    L2.sort(reverse=True)
    return L1, L2


# print(random_list_V3())