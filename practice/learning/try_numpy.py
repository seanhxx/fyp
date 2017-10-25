import numpy

array_1 = numpy.array([[[1,2,3],
                        [0,0,0],
                        [0,2,4]],
                       [[2,3,4],
                        [1,1,1],
                        [2,4,6]]])
array_2 = numpy.array([[[3,4,5],
                        [2,2,2],
                        [1,3,5]],
                       [[4,5,6],
                        [3,3,3],
                        [3,5,7]]])

a = numpy.concatenate((array_1, array_2), axis = 0)
print(a.shape)