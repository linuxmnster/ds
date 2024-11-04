def pivot_place(array,first,last): 
    pivot=array[first] 
    left=first+1 
    right=last 
    while(True): 
        while(left<=right and array[left]<=pivot): 
            left=left+1 
        while(left<=right and array[right]>=pivot): 
            right=right-1 
        if(right<left): 
            break 
        else: 
            array[left],array[right]=array[right],array[left] 
    array[first],array[right]=array[right],array[first] 
    return right
 
def quicksort(array,first,last): 
        if(first<last): 
            p=pivot_place(array,first,last) 
            quicksort(array,first,p-1) 
            quicksort(array,p+1,last) 
            
array=[50,20,10,1,100] 
n=len(array) 
print("Before sorting array is:",array)  
quicksort(array,0,n-1) 
print("After sorting array is:",array)