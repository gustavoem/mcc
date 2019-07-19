import ray
import time

ray.init()

@ray.remote
def add(x, y):
    time.sleep(1)
    return x + y


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

some_sum = add.remote(19, 19)
print(some_sum)

while len(values) > 1:
    values = values[2:] + [add.remote(values[0], values[1])] 

total = ray.get(values[0])
print(total)
