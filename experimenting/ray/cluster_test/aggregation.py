import ray
import time
import sys

redis_ip = sys.argv[1]

ray.init(redis_address=redis_ip)
@ray.remote
def add(x, y):
    time.sleep(1)
    return x + y


values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

some_sum = add.remote(19, 19)
print(some_sum)

while len(values) > 1:
    values = values[2:] + [add.remote(values[0], values[1])] 

resources = ray.get_resource_ids()
print("Resources:", resources)

nodes = ray.nodes()
print("Nodes:", nodes)

total = ray.get(values[0])
print(total)
