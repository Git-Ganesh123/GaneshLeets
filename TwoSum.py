class Solution(object):
    def twoSum(self, nums, target):
        indices = []

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                
                if len(indices) == 0 and i != j:
                    if (x + y) == target:
                        indices.append(i)
                        indices.append(j)
            
        return indices

# low memory consumption
# but high runtime

        
