import ssorrt 
import time
import random
N=int(input())
Massiv = [random.randint(1,100000) for i in range(N)]
Start = time.time()
ssorrt.bubblesort(Massiv)
Finish = time.time()
Res_msec = (Finish-Start)
print(Res_msec)
