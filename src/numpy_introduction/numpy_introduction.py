import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0, 5.5])
print(x)
print(type(x))

my_list1 = [1,2,3,4,5]
my_array1 = np.array(my_list1)
print(my_array1)

my_list2 = [10,20,30,40,50]
my_lists = [my_list1, my_list2]
print(my_lists)

my_array2 = np.array(my_lists)
print(my_array2)

print(my_array1.shape)
print(my_array2.shape)

x = np.arange(10)
print(x)

x = np.arange(1, 10).reshape(3,3)
y = np.arange(1, 10).reshape(3,3)

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)

sample_array3 = np.array([[1,2,3],[4,5,6]])
sample_array4 = np.array([[7,8,9],[10,11,12]])

print(np.concatenate([sample_array3,sample_array4],axis=1))
print(np.hstack((sample_array3,sample_array4)))

print(np.concatenate([sample_array3,sample_array4],axis=0))
print(np.vstack((sample_array3,sample_array4)))

sample_array = np.arange(10)
print(sample_array)
print(sample_array + 5)

n1 = np.array([1,2,3,4,5])
print(n1)
print(np.ndim(n1))
print(n1.shape)

'''
[1.  2.  3.  4.  5.5]
<class 'numpy.ndarray'>
[1 2 3 4 5]
[[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
[[ 1  2  3  4  5]
 [10 20 30 40 50]]
(5,)
(2, 5)
[0 1 2 3 4 5 6 7 8 9]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
[[0 0 0]
 [0 0 0]
 [0 0 0]]
[[ 1  4  9]
 [16 25 36]
 [49 64 81]]
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
[[ 1  2  3  7  8  9]
 [ 4  5  6 10 11 12]]
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
[0 1 2 3 4 5 6 7 8 9]
[ 5  6  7  8  9 10 11 12 13 14]
[1 2 3 4 5]
1
(5,)
'''
