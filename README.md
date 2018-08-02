# 1-D SPIHT Algorithm
A implementation of the SPIHT algorithm for compressing a 4-level discrete wavelet transform using Python
by: Gunnar Pope
email: gunnar.c.pope.th@dartmouth.edu

Input:

A 1-D vector of the Approximation and Detail coefficient vectors

Output:

A binary stream of 1's and 0's representing the SPIHT encoding of the WT vector.

This algorithm was coded in python from the SPIHT algorthm described in: Pooyan, M., Taheri, A., Moazami-Goudarzi, M., & Saboori, I. (2004). Wavelet compression of ECG signals using SPIHT algorithm. International Journal of signal processing, 1(3), 4.
and Lu, Z., Kim, D. Y., & Pearlman, W. A. (2000). Wavelet compression of ECG signals by the set partitioning in hierarchical trees algorithm. IEEE transactions on Biomedical Engineering, 47(7), 849-856.


Definitions
* x[i]: any wavelet coefficient in the 1D multilevel wavelet transformation
* O[i]: the set of 2 coefficients of the next higher subband from coefficient x[i]
* D[i]: the set containing all offsprint in all later subbands
* L[i]: a set defined by L[i] = D[i] - O[i]
* S_k[x_i]: the significance of x[i] with respect to a threshold k, where
*     S_k[x_i] = 1 iff |x_i| >= 2^k and is 0 otherwise
* LIP = the List of Insignificant Points which contains the coordinates of those coefficients
*   that are insignificant wrt the current threshold of k
* LSP =  the List of Significant Points which contains the coordinates of those coefficients
  that are significant wrt the current threshold of k
* LIS =  the List of Insignificant Sets which contains the coordinates of of the roots of insignificant subtrees
  LIS has two types, A and B, relating to the cases D[i] and L[i], respectively.


