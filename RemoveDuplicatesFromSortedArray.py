class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        pointer = 1
        if len(nums) == 1:
            return 1
        while pointer < len(nums):
            if nums[pointer] != nums[pointer-1]:   # if seeing for first time, assign value in pointer to value in left
                nums[left] = nums[pointer]
                left+=1
                pointer+=1
            else:   # if not seeing first time, i.e if duplicate, move the pointer and keep left the same 
                pointer+=1
        return left
        
        # Keep two pointer, one to store where to put the new value(left) and one more to parse the array(pointer)
        
        


        
