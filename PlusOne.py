class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[len(digits)-1] != 9: 
            digits[len(digits)-1] = digits[len(digits)-1] + 1
            return digits

        needsChange = True     # tells whether carry forward has been accounted or not
        result = []

        for i in digits[::-1]:
            if i == 9 and needsChange:      # carry forward has not been accounted yet 
                result.insert(0,0)                
            else:
                if needsChange: 
                    result.insert(0,i+1)
                    needsChange = False        # carry forward of 1 has been accounted in previous step
                else:   # digit doesnt need any change, carry forward of 1 has already been accounted 
                    result.insert(0,i) 

        if i == 9 and needsChange:   # the first digit needs to be checked for carry forward 
            result.insert(0,1)      

        return result 
        
