def binary(arr,target):
    arr.sort()
    low = 0
    high= len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:

            high= mid -1
        else:
            low=mid +1
    return -1
arr=[1,2,34,5,6,78,7]    

target=2 
print(binary(arr,target))      





    

