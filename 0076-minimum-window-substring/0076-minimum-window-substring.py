class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        need = Counter(t)
        match = 0
        l, start, length = 0, 0, len(s) + 1

        for r, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                match += need[ch] == 0
            while match == len(need):
                if length > r - l + 1:
                    start, length = l, r - l + 1
                remove = s[l]
                l += 1
                if remove in need:
                    match -= need[remove] == 0
                    need[remove] += 1
        if length <= len(s):
            return s[start:start + length] 
        return ''
            


        