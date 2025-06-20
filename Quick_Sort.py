
import time
import random

def quick(arr):
    if len(arr)<=1:
        return arr
    piv = arr [len(arr)//2]
    low = [i for i in arr if i < piv]
    mid = [ i for i in arr if i == piv]
    high =[ i for i in arr if i > piv]



    return quick(low) + mid + quick(high)

def calc_time(n,arr):

   #Average Case Complexity
   start = time.time ()
   quick(arr)
   avg_time =time.time () - start

   #Best Case Complexity
   start = time.time ()
   quick(arr)
   best_time =time.time () - start

   #Worst Case Complexity
   start = time.time ()
   quick(arr)
   Worst_time =time.time () - start

   return n, best_time ,avg_time ,Worst_time



user_ip = [random.randint(1,10000) for _ in  range(51)]
print("n\tbest_time,\tavg_time,\tworst_time")
for n in user_ip:
    arr = [random.randint(1,1000) for _ in range(n)]
    n, best_time, avg_time, worst_time = calc_time(n,arr)
    print(f"{n}\t{best_time:.8f}\t{avg_time:.8f}\t{worst_time:.8f}")

