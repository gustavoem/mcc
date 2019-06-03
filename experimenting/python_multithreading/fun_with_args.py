from multiprocessing import Pool
import multiprocessing
import random

# This solution is inspired on the solution of klaus se on the Stack 
# Overflow thread:
# https://stackoverflow.com/questions/3288595/multiprocessing-how-to-use-pool-map-on-a-function-defined-in-a-class

def fun_runner(f, q_in, q_out):
    while True:
        i, x = q_in.get()
        if i is None:
            break
        q_out.put((i, f(x)))


def parmap(f, X):
    nprocs = 4
    q_in = multiprocessing.Queue (1)
    q_out = multiprocessing.Queue ()

    proc = [multiprocessing.Process(target=fun_runner, args=(f, q_in, 
        q_out)) for _ in range(nprocs)]

    for p in proc:
        p.daemon = True
        p.start ()
    
    sent = [q_in.put ((i, x)) for i, x in enumerate (X)]
    [q_in.put ((None, None)) for _ in range (nprocs)]
    [p.join () for p in proc]
    res = [q_out.get () for _ in range(len(sent))]

    return [x for i, x in sorted (res)]


print (parmap (lambda i : i * 2, [1, 2, 3, 4, 5, 6]))
