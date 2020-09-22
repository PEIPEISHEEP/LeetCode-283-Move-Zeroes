class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dic={}
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
                dic[c]=i
        c2=c
        for i in range(c):
            nums.pop(dic[c2])
            nums.append(0)
            c2 -= 1
            