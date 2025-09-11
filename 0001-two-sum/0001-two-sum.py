class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    return l """
        d={}
        l=[]
        for i,value in enumerate(nums):
            
            if target-value in d:
                l.append(i)
                l.append(d[target-value])
                return l
            if value not in d:
                d[value]=i