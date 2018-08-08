# spiht_sets.py
# by: gunnar pope



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

    return sorted(flatten(descendents,a=[]))

def L(i,N):
    """Remove the first """
    return D(i,N)[2:]

def flatten(l, a):
    """
    print(flatten([ [[1, [1,1, [3, [4,5,]]]], 2, 3], [4, 5],6 ] , []))
    # [1, 1, 1, 3, 4, 5, 2, 3, 4, 5, 6]
    """
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a




if __name__ == '__main__':

    print("Find the descendents for a 32 element dwt with dyadic scalling")
    N = 32
    for i in range(17):
        print(i, O(i,N))

    print("Find the descendents of index=3, ie D(3)")
    i = 3
    print('O(i): ', O(i,N))
    print('D(i): ', D(i,N))
    print('L(i): ',L(i,N))
