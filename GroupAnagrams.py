class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26 # for each string, initialize an empty list which will hold frequency of character count index wise
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()
      
'''
idea is to get a character count for each string of input. Make this character count as key of result dic, and every string which has same character count, 
put it insdie the list which is value for that key. 

My earlier solution was sorting it and adding the sorted tuple as a key of the dictionary. This is O(m*nlogn). Slower than this solution which is 

O(m*n)
m = number of strings
n = avg size of each string
'''
