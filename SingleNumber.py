class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for i in nums:
            ans = ans^i
        return ans

        '''
        https://www.youtube.com/watch?v=qMPX1AOa83k
  
        impossible to think of this solution, just have to know it. Bit manipulation. 
        '''
