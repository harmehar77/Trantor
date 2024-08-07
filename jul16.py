#MULTI-THREADING 

#multi threading using threading module(old method)
import threading
import time 

starting= time.perf_counter()

def do_something(sec):
    print(f"sleeping for {sec} second(s)")
    time.sleep(sec)
    print(f"slept for {sec} second(s)")
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args = [2])
    t.start()
    threads.append(t)

for thread in threads:
    t.join()


finishing= time.perf_counter()
print(f"Time taken for execution: {round(finishing-starting,3)} sec")

#threading using thread pool executor method
import concurrent.futures
import time

starting= time.perf_counter()

def do_something(sec):
    print(f"sleeping for {sec} second(s)")
    time.sleep(sec)
    return f"slept for {sec} second(s)"

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    
    results = executor.map(do_something,secs)

    for result in results:
        print(result)

    results = [executor.submit(do_something, sec) for sec in secs]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finishing= time.perf_counter()
print(f"Time taken for execution: {round(finishing-starting,3)} sec.")

import concurrent.futures
import time
st = time.perf_counter()
def cube(n):
    print(f"Cube of {n} = {n*n*n}")
    #return f'Cube of {n} is {n**3}'
nums = [2,3,4,5,6,7]
for i in nums:
    print(cube(i))
with concurrent.futures.ThreadPoolExecutor() as executor:
    #results = []
    nums = [2,3,4,5,6,7]
    
    results = executor.map(cube,nums)
    for result in results:
        print(result)
    
    for r in results:
        print(r)
    results = [executor.submit(cube,num) for num in nums]

    for r in concurrent.futures.as_completed(results):
        print(r.result())

ft = time.perf_counter()
print(f"Execution time: {round(ft-st,3)} secs.")