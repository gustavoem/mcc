import numpy as np
import ray

ray.init()

@ray.remote
def create_matrix(size):
    return np.random.normal(size=size)

@ray.remote
def multiply_matrices(A, B):
    return np.dot(A, B)

A_id = create_matrix.remote([1000, 1000])
B_id = create_matrix.remote([1000, 1000])
C_id = multiply_matrices.remote(A_id, B_id) 

C = ray.get(C_id)
print(C)

