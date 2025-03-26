#find min in rotated sorted array

#binary search 
def findMin(self, nums: List[int]) -> int:
    #res is the value to find
    res = nums[0]

    #define left/right pointers and length 
    l, r = 0, len(nums) - 1

    #if the current range is already sorted, the leftmost value is smallest
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        #case 2- calculate middle value 
        m = (l + r) //2

        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            #search left half
            r = m - 1
        return res
    
    #this continues until the minimum value is found 
    # O(logn)

