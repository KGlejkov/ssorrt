import ssorrt
import time
import random

a=[10,100,1000,10000,10**7]
mas=[]
for j in a:
    mas.append([random.randint(-100,100) for _ in range(n)])
    print(n)
st=time.time()
print(start)
#sort.bubblesort(mas[1])
#sort.selectsort(mas[3])
#sort.insertionsort(mas[3])
sort.quicksort(mas[4],0,len(mas[4])-1)
#sort.cocktailsort(mas[3])
end=time.time()
print(end)
t0=end-st
print(t0)
