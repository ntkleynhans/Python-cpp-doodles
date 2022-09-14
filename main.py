import asyncio
import time
import random
import numpy as np
import ctypes
import array

mylib = ctypes.CDLL('mysum.dylib')

# CONSTANTS
LEN = 1_000_000

VALUES = [random.random() for x in range(LEN)]

# SETUP
test_passing_array = mylib.test_passing_array
test_passing_array.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
test_passing_array.restype = ctypes.c_double

# FUNCTIONS
def simple_sum():
    total = 0
    start_t = time.perf_counter()
    for i in range(LEN):
        total += VALUES[i]
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"Simple: {duration=} {total=}")


def unroll_sum():
    acc = [0.0]*4
    start_t = time.perf_counter()
    k = 0
    for i in range(int(LEN/4)):
        acc[0] += VALUES[k]
        acc[1] += VALUES[k+1]
        acc[2] += VALUES[k+2]
        acc[3] += VALUES[k+3]
        k = k + 4
    print(f"{k=}")
    total = sum(acc)
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"Unroll: {duration=} {total=}")

def numpy_sum():
    #vals = np.array(VALUES, dtype=np.float64)
    vals = np.fromiter(VALUES, dtype=np.float64)
    start_t = time.perf_counter()
    total = vals.sum()
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"Numpy: {duration=} {total=}")

def mysum_sum():
    #data = (ctypes.c_double * LEN)(*VALUES)
    val_a = array.array('d', VALUES)
    data = (ctypes.c_double * LEN).from_buffer(val_a)
    start_t = time.perf_counter()
    total = mylib.test_passing_array(data, LEN)
    end_t = time.perf_counter()
    duration = end_t - start_t
    print(f"Mysum: {duration=} {total=}")


if __name__ == "__main__":
    simple_sum()
    unroll_sum()
    numpy_sum()
    mysum_sum()
