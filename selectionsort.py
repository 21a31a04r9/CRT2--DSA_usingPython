def performselectionSort(nums):
    n=len(nums)
    fixThisIndex=n-1

    while fixThisIndex>0:
        maxEleIndex=fixThisIndex #lastele
        
         #below part of code is finding the  max ele index
        for index in range(maxEleIndex):
            if nums [index] > nums[maxEleIndex]:
                maxEleIndex=index

        if maxEleIndex!=fixThisIndex:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisIndex]
            nums [fixThisIndex] = temp
        print(nums)
        fixThisIndex-=1

nums=[10, 8, 2, 14, 12, 7]
print("Before sorting:", nums)
performselectionSort(nums)
print("After sorting:", nums)

