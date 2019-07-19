import ray
import time


ray.init()

@ray.remote
def f(x):
    time.sleep(1)
    return x

result_ids = []
for i in range(4):
    result_ids.append(f.remote(i))

result = ray.get(result_ids)
print(result)
