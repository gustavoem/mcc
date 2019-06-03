# Following the article: 
# https://chriskiehl.com/article/parallelism-in-one-line

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import urllib.request as urlrequest
import random
import numpy


def time_consuming_function (x):
    for i in range (1000000):
        x += numpy.exp (-x)

pool =  ThreadPool (2)

numbers = [random.randrange (1, 10) for i in range (10)]

pool = Pool(4)
results = pool.map(time_consuming_function, numbers)
pool.close()
pool.join()

