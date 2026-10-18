class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i,n in enumerate(nums):
       
            for j,k in enumerate(nums):
                if n+k != target or i==j:
                    continue
                else: 
                        return [i,j]      