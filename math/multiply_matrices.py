# Reference: https://www.mathsisfun.com/algebra/systems-linear-equations-matrices.html
# 
# Let's say we have a system of linear equations that looks like this
# x + y + z = 6
# 2y + 5z = −4
# 2x + 5y − z = 27
#
# This can be represented by the matrices
# | 1 1  1 | | x |   |  6 |
# | 0 2  5 | | y | = | -4 |
# | 2 5 -1 | | z |   | 27 |
#
# This has the form AX = B
# Then we have X = A^(-1)B
# 
# Let's use python and the numpy library to get a solution

import numpy

print('Consider the system of equations:')
print('x + y + z = 6')
print('2y + 5z = −4')
print('2x + 5y − z = 27')

print('\nGeneral form: AX = B')

A = ([1,1,1], [0,2,5], [2,5,-1])
print('\nMatrix A = {}'.format(A))

B = ([6,-4,27])
print('\nMatrix B = {}'.format(B))

print('\nMatrix X =  [x,y,z]')

A_inverse = numpy.linalg.inv(A)
print('\nA^(-1) = \n{}'.format(A_inverse))

X = numpy.dot(A_inverse, B)

print('\nX = A^(-1)B = \n{}'.format(X))