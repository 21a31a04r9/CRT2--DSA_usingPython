def performsinsertionsort(nums):
    n=len(nums)
    lastEleInSortedArr=0
    for firstindex in range(1,n):
            temp=nums[firstindex]
            previous=lastEleInSortedArr
                
    #7,13,34,9
    while previous>=0 and nums[previous]>temp:
        nums[previous+1]=nums[previous]
        previous-=1
    nums[previous+1]=temp
    lastEleInSortedArr+=1
        

nums=[10, 8, 2, 14, 12, 7]
print("Before sorting:", nums)
performsinsertionsort(nums)
print("After sorting:", nums)

