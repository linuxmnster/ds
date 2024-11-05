def mergesort(array): 
    if(len(array)>1): 
        mid=len(array)//2 
        leftlist=array[:mid] 
        rightlist=array[mid:] 
        mergesort(leftlist) 
        mergesort(rightlist) 
        i = j = k = 0
        while(i<len(leftlist) and j<len(rightlist)): 
            if(leftlist[i]<rightlist[j]): 
                array[k]=leftlist[i] 
                i=i+1 
                k=k+1 
            else: 
                array[k]=rightlist[j] 
                j=j+1 
                k=k+1 
        while(i<len(leftlist)): 
            array[k]=leftlist[i] 
            i=i+1 
            k=k+1 
        while(j<len(rightlist)): 
            array[k]=rightlist[j] 
            j=j+1 
            k=k+1 

n=int(input("How many numbers in array: ")) 
array=[int(input())for x in range(n)] 
mergesort(array) 
print("After sorting array is:",array)
