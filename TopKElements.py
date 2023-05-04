class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        tempList = [ [] for _ in range(len(nums)+1)]

        result = []
        for p,v in dic.items():
            tempList[v].append(p)

        for i in range(len(nums),0,-1):
            if len(tempList[i]) != 0:
                result.extend(tempList[i])
            if len(result) == k:
                return result
    
 '''
 O(n) space complexity 
 O(n) size xomplexity
 n = number of unique elements 
 ''' 
