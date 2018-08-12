# spiht.py
# An implementation of the SPIHT algorithm used to compress a 1-D Discrete Wavelet Transform vector
# by: Gunnar Pope
# email: gunnar.c.pope.th@dartmouth.edu

# Input:
# a 1-D vector of the Approximation and Detail coefficient vectors

# Output:
# a binary stream of 1's and 0's representing the SPIHT encoding of the WT vector

# see Pooyan, et al. 2005, 'Wavelet Compression of ECG Signals Using SPIHT Algorithm for details
# regarding the algorithm proceedure.

# Definitions
# x[i]: any wavelet coefficient in the 1D multilevel wavelet transformation
# O[i]: the set of 2 coefficients of the next higher subband from coefficient x[i]
# D[i]: the set containing all offsprint in all later subbands
# L[i]: a set defined by L[i] = D[i] - O[i]
# S_k[x_i]: the significance of x[i] with respect to a threshold k, where
#     S_k[x_i] = 1 iff {|x_i| >= 2^k and 0 otherwise

# LIP = the List of Insignificant Points which contains the coordinates of those coefficients
#   that are insignificant wrt the current threshold of k

# LSP =  the List of Significant Points which contains the coordinates of those coefficients
#   that are significant wrt the current threshold of k

# LIS =  the List of Insignificant Sets which contains the coordinates of of the roots of insignificant subtrees
#   LIS has two types, A and B, relating to the cases D[i] and L[i], respectively.


from spiht_dyadic import O, D, L, get_ODL


def find_mldwt_vector_lenghts(signal,wavelet,level,mode):

    coeffs = wavedec(signal, wavelet,level=level,mode=mode )
    print("The length of the vectors [A4,D4,..,D1] are:")
    lengths = []
    for vec in coeffs:
        lengths.append(len(vec))
    return lengths

def S(x, k):
    """Compare value x to the threshold 2^k
       Input: a signed integer, x
       Output: 1 if |x| >= 2^k
               0 if not """

    if  np.abs(x) >= 2**k:
        print ('Threshold= ', 2**k)
        thres = 1
    else:
        thres = 0
# todo: maybe implement bitwise threshold comparison?
    # >> > bin(a | int('0b010', 2))
    # '0b11111'
    # >> > bin(a & int('0b010', 2))
    # '0b0'

    return thres

def D_dyadic(index, level):
    """
    Inputs:
        int index = indicies of coefficient vector of A5, D5, etc.. starting from index=0
        int level = the transformation level, ranging from level to 1
    Output:
        Returns a list of sets that are the offspring of x[i]
    """
    offspring_sets = []
    nextlevel = level - 1
    first = 2*index
    second = first + 1
    offspring_sets.append([first, second])

    # todo: add recursive search for coeffs
    return offspring_sets

def Dsym(index, level, dwt_coef_lengths):
    print('todo:...')


def get_lists():
    print ('The LIP is:'  , lip)
    print ('The LIS is: ' , lis)
    print ('The LSP is: ' , lsp)
    print ('The output is:', strout)



def signbit(x):
    """ Returns 1 if x<0"""
    return int(x < 0)

def get_LIS_index_and_type(LIS_entry):
    """Input: a LIS entry in the form of ['A', index]
       output: [ type, index]
    """
    type  = LIS_entry[0]
    index = LIS_entry[1]

    return [ type, index]

def output(bit):
    global strout
    global step

    strout += str(bit)
    print('Step: ', step)
    print('Output String: ', strout)
    get_lists()


#******************************************************************************************
#******************************************************************************************

if __name__ == "__main__":

    import numpy as np
    from pywt import wavedec




    import matplotlib.pyplot as plt
    # import a 1D wavelet vector taken from an EDA signal
    # x = np.load('wavelet_vector.npy')
    # print('This is A5: ',x[:12])
    # print('This is D5: ', x[12:24])
    # plt.plot(x)
    # plt.show()

    # get lengths of all A4, D4,..,D1 vectors
    sig = [x for x in range(128)]

    # Vector from Lu et al. 2000, "Wavelet Compression of ECG Signals by the SPIHT Algorithm", p851
    # this is a 4-level dwt that uses no padding and dyadic scaling
    x = [59,-48,-25,21,12,13,-9,11,43,-7,8,6,-5,4,2,-3,22,11,5,-7,6,1,5,2,0,-2,-1,4,4,-2,3,1]

    # the length of the A4,D4,D3,D2,D1 vectors
    dwt_coeff_len = { 'A4' : 2,
                      'D4' : 2,
                      'D3' : 4,
                      'D2' : 8,
                      'D1' : 16}
    print(dwt_coeff_len)

    dwt_levels = 4

    # get the starting indicies of the coefficient vectors A4,D4, etc...
    starting_xind = [0,4,8,16]
    max_len = len(x)

    # the lengths are defined by len(LEVEL)/2+2 = len(LEVEL+1)
    vec_lengths = find_mldwt_vector_lenghts(sig,'db3',4,'symmetric')
    print(vec_lengths)


# Begin the SPIHT algorithm
    lip  = []
    lsp  = []
    strout = ''


# STEP 0
    # find the length of the wt vector
    step = 0
    # find the threshold, k
    k = int(np.abs(np.log2(np.max(np.abs(x)))))

    strout += format(k, '04b')
    strout += ' '                   # add a space for readability
    print('Threshold, K= ',k)
    lsp = []

# todo: need to fix this function to account for the correct length of A4 and D4
    # lip = [ x for x in range(dwt_coeff_len['A4'])] # the set of all roots coordinates in the top-most lowpass subband
    lip = [ x for x in range(4)] # the set of all roots coordinates in the top-most lowpass subband

    lis = [ ['A', x] for x in lip[-2:]]

    get_lists()

while (k > 0):
    # STEP 1: SORTING PASS IN LIP
    step += 1
    index_to_append = []
    for i in lip:

        # check the threshold
        thres =  S(x[i],k)
        # strout += str(thres)
        output(thres)

        if thres > 0:
            # output the sign bit (1 if x<0)
            # strout += str(signbit(x[i]))
            output(signbit(x[i]))

            # add i to LSP and pop from LIP
            index_to_append.append(i)


    # only do this after the iteration in lip is finished
    for i in index_to_append:
        lsp.append(i)
        ind = lip.index(i)
        lip.pop(ind)


    # add a space for readability, but todo: remove this later
    strout += ' '

# STEP 2: SORTING PASS IN LIS
    step += 1
    lis_index = 0
    sorting_indices_used = []

    while ( lis_index < len(lis) ):             # step 5

        (type, i) = lis[lis_index]

        if type == 'A':

            # test the threshold and send a 1 if significant


            # find out if any descendents are significant (either 1 or 0)
            sig_descendents = max([ S(x[p],k) for p in D(i,max_len)])
            print('D(c[i]): ', sig_descendents, ' i= ', i)

            if (sig_descendents >0  ): #step 7
                output(1)

                for j in O(i,max_len):

                    output( S(x[j],k) )

                    if (thres > 0):
                        lsp.append(j)
                        output(signbit(x[j]))
                    else:
                        lip.append(j)          # step 12


                    sorting_indices_used.append(j)

                print('L(i,max_len): ', L(i,max_len), ' i= ', i)
                if ( L(i,max_len) == []):
                    # remove i from LIS
                    lis.pop(lis_index)          # step 14
                else:

                    lis.pop(lis_index)          # remove entry from front on LIS list
                    lis.append(['B', i])        # append it to the end of the LIS as type-B entry
                    lis_index = 0               # restart the LIS loop from the beginning
                    get_lists()
                    continue                       # go to step 5
            else:
                output(0)
                lis_index += 1





        elif ( type == 'B'):
            # strout += str( max([S(x[p], k) for p in L(i, max_len)] )    # step 17
            thres = max([S(x[p], k) for p in L(i, max_len)])   # step 17
            print('S(L[i]): ',thres)
            output( thres )

            if (thres > 0):
                for j in O(i,max_len):
                    lis.append( ['A', j] )      # step 19
                lis.pop(lis_index)
                lis_index -= 1                  # this is needed to account for popping an entry from the list

            lis_index += 1

    # Refinement pass
    # for i in lsp:
    #     # exclude indices used in the sorting pass
    #     if ( i in sorting_indices_used):
    #         # output the kth bit of |x[i]|
    #         # to a binary AND with a single bit
    #         # a = -5 = -0b101 --> abs(a) & (1 << 1) = 0
    #         # a = -5 = -0b101 --> abs(a) & (1 << 2) = 4
    #         kbit = abs(x[i]) & (1 << (k-1))
    #         if kbit > 0:
    #             output(1)
    #         else:
    #             output(0)

    get_lists()
    # k -= 1
    k = 0  # used to stop the interation



