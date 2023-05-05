class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(i-dic[nums[i]]) <= k:
                    return True
            dic[nums[i]] = i
        return False
      
 '''
 first check if element in dic
 if yes, check its value(index) -> if abs value of difference of indexes is <= k, return true
 if not in dic, add in dic
 
 space complexity -> O(n)
 size complexity -> O(n)
 '''
