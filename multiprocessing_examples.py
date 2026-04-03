import multiprocessing
import os
import time

def worker1():
    print(f"Worker process id: {os.getpid()}")

def square(x):
    return x * x

def worker2(num, arr, index):
    num.value += 1
    for i in range(len(arr)):
        arr[i] = arr[i] + index  # Modify the shared array uniquely per process


if __name__ == "__main__":
    """
    #example 1
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=worker1)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    """
    """
    #example 2
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(1000000))
        #print(results)
    end_time = time.time()
    print(end_time - start_time)
    """
    """
    #to compare sequential computing for large N to parallel computing across 4 processes
    start_time = time.time()
    results = []
    for i in range(1000000):
        results.append(square(i))
    #print(results)
    end_time = time.time()
    print(end_time - start_time)
    """

    num = multiprocessing.Value('i', 0)  # Shared integer value
    arr = multiprocessing.Array('i', range(10))  # Shared array

    processes = []
    num_processes = 5  # Number of processes to start

    # Create and start multiple processes
    for i in range(num_processes):
        p = multiprocessing.Process(target=worker2, args=(num, arr, i))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("Final num value:", num.value)
    print("Final arr values:", arr[:])








