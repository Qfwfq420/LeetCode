class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1, l2, result = [], [], []
        for num in nums:
            if num > 0:
                l1.append(num)
            else:
                l2.append(num)
        for i in range(len(l1)):
            result.append(l1[i])
            result.append(l2[i])
        return result

        