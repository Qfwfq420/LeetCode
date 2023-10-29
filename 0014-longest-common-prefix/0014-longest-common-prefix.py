class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0]
        for i in range(1, len(strs)):
            result = result[:len(strs[i])]
            for j in range(1, len(strs[i]) + 1):
                if result[:j] != strs[i][:j]:
                    if j == 1:
                        return ''
                    else:
                        result = strs[i][:j-1]
                        break
        return result

        

        