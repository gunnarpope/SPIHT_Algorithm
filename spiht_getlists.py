# spiht_sets.py


def O(i,N):
    offspring1 = i*2
    offspring2 = offspring1 + 1

    if i < 2:
        output = []

    elif (offspring2 > (N-1)):
        output = []
    else:
        output = [offspring1, offspring2]
    return output

def D(i,N):
    descendents = []

    offspring = O(i,N)

    for j in offspring:
        descendents.append(j)

        if j < ((N-1)/2):
            descendents.append( D(j,N) )

    return flatten(descendents,a=[])

def flatten(l, a):
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a




if __name__ == '__main__':

    import numpy as np
    print("Find the descendents for a 32 element dwt with dyadic scalling")
    N = 32
    for i in range(17):
        print(i, O(i,N))

    print("Find the descendents of index=3, ie D(3)")
    i = 3
    output = D(i,N)
    print(output)

