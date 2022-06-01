Problem
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns.
Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. 
Their profile matrix is a 4×n matrix P in which P1,
j represents the number of times that 'A' occurs in the jth position of one of the strings,
P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position;
the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix.
Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
