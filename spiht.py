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

    return thres

def get_LIP():
    print ('The LIP is:', lip)

def get_LISA():
    print ('The LISA is: ',lisa)

def signbit(x):
    """ Returns 1 if x<0"""
    return int(x < 0)


#******************************************************************************************
#******************************************************************************************

if __name__ == "__main__":

    import numpy as np
    from pywt import wavedec




    import matplotlib.pyplot as plt
    # import a 1D wavelet vector taken from an EDA signal
    x = np.load('wavelet_vector.npy')
    # plt.plot(x)
    # plt.show()

    # get lengths of all A4, D4,..,D1 vectors
    sig = [x for x in range(128)]

    # Vector from Lu et al. 2000, "Wavelet Compression of ECG Signals by the SPIHT Algorithm", p851
    x = [59,-48,-25,21,12,13,-9,11,43,-7,8,6,-5,4,2,-3,22,11,5,-7,6,1,5,2,0,-2,-1,4,4,-2,3,1]
    # get the starting indicies of the coefficient vectors A4,D4, etc...
    starting_xind = [0,4,8,16]
    max_len = len(x)
    approx_len = 4
    wt_levels = 3

    # vec_lengths = find_mldwt_vector_lenghts(sig,'db3',4,'symmetric')
    # print(vec_lengths)

    # # get the starting indicies of the coefficient vectors A4,D4, etc...
    # starting_xind = [0,12,24,44,79]




# Begin the SPIHT algorithm
    lip  = []
    lsp  = []
    lisa = []
    lisb = []

    strout = ''


# STEP 1
    # find the length of the wt vector

    # find the threshold, k
    k = int(np.abs(np.log2(np.max(np.abs(x)))))
    # print('Threshold',k)
    lsp = []
    lip = [ x for x in range(approx_len)] # the set of all roots coordinates in the top-most lowpass subband

    lisalen = approx_len/2
    lisa = lip[-2:]

# STEP 2: SORTING PASS
    for i in lip:

        # check the threshold
        thres =  S(x[i],k)
        strout += str(thres)

        if thres > 0:

            strout += str(signbit(x[i]))



    get_LIP()
    get_LISA()
    print('Step2 output:', strout)
    # WORKS TO HERE

# STEP 3:
