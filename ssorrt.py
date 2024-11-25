from sys import setrecursionlimit as lim
lim(3000)

def bubblesort(a):
    n=len(a)
    unordered=True
    while unordered:
        unordered=False
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                unordered=True
        n-=1
    return a

def selectsort(a):
    for i in range(len(a)-1):
        imin=i
        for j in range(i+1,len(a)):
            if a[j]<a[imin]:
                imin=j
        a[i],a[imin]=a[imin],a[i]
    return a

def insertionsort(a):
    for i in range(1,len(a)):
        tmp=a[i]
        j=i-1
        while j>=0 and a[j]>tmp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=tmp
    return a

def quicksort(a,l,h):
    if l<h:
        pivotindex=partition(a,l,h)
        quicksort(a,l,pivotindex-1)
        quicksort(a,pivotindex+1,h)
def partition(a,l,h):
    pivot=a[l]
    i=l+1
    for j in range(l+1,h+1):
        if a[j]<=pivot:
            a[i],a[j]=a[j],a[i]
            i+=1
    a[l],a[i-1] = a[i-1],a[l]
    return i-1

def cocktailsort(a):
    n=len(a)
    swapp=True
    st=0
    end=n-1
    while swapp==True:
        swapp=False
        for i in range (st, end):
            if a[i] > a[i+1] :
                a[i], a[i+1]= a[i+1], a[i]
                swapp=True
        if swapp==False:
            break
        swapp=False
        end=end-1
        for i in range(end-1, st-1,-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapp=True
        st=st+1
    return a
