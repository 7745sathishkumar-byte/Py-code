def binary_search(arr,a,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==a:
            return mid
        elif arr[mid]>a:
            return binary_search(arr,a,low,mid-1)
        else:
            return binary_search(arr,a,mid+1,high)
    else:
        return -1
arr=[1,2,3,4,5,6,7,8,9]
print("The array given is:",arr)
a=8
print("The element to be found:",a)
index=binary_search(arr,a,0,len(arr)-1)
if(index!=-1):
    print("The index position of an element:"+str(index))
else:
    print("Not found")
