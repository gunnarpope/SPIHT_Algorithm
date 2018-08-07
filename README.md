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

## Step 1:
compute and output k, where k is k = |log2(max(x))|

from userguide p270


Since the msp430 "...hardware multiplier has two 32-bit operand registers – operand one (OP1) and operand two (OP2),
and a 64-bit result register accessible through registers RES0 to RES3. For compatibility with the 16×16
hardware multiplier, the result of a 8-bit or 16-bit operation is accessible through RESLO, RESHI, and
SUMEXT, as well. RESLO stores the low word of the 16×16-bit result, RESHI stores the high word of the
result, and SUMEXT stores information about the result."

Therefore, the max fixed point float is a 32-bit number with the decimal at bit 15 and a signed bit at bit 32. Thus the max magnitude is 15 bits. log2(2^(15-1) = 16384.

* The max output of k is 2^k = 15 = b'1111' , which can be represented in 4 bits. Therefore, the output from step 1 will be 4 bits.




