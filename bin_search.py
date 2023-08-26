# binary search implementation

# function to perform binary search
def binary_search(array , key):
    low = 0
    high = len(array)-1
    
    while(high-low>1):
        mid = int((high-low)/2)
        if array[mid]==key:
            return mid
        elif key > array[mid]:
            low = mid+1
        else:
            high = mid-1
    return None


array = [1,2,3,6,8,22,45,68,97,86,102,148,161,229,278,356,498,512]
key = 6

print(binary_search(array,key))

