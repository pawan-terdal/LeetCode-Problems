class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return l

        '''
        this is basically binary search, if nothing is found, we return the left pointer. why ? 
        in case the target needs to be put outside the array rught side, the last loop of binary search
        will do l+1 on the right most element and then exit the loop, so thats correct
        in case the element needs to be put at the left end of array, so again the loop ends when we 
        do r - mid - 1, so left index is where the new element will be stored. 
