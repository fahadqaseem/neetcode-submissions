class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # Value of difference maps to indices.  Difference ---> Indice. 

        for indice, num in enumerate (nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], indice]
            seen[num] = indice
            

