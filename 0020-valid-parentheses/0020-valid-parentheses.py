class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = True
        bra = True
        aco = True
        parnum = 0
        branum = 0
        aconum = 0
        last = []
        for x in s:
            if x == '(':
                par = False
                parnum += 1
                last.append('par')
            elif x == '[':
                bra = False
                branum += 1
                last.append('bra')
            elif x == '{':
                aco = False
                aconum += 1
                last.append('aco')
            elif x == '}':
                if aco:
                    return False
                elif last[-1] == 'aco':
                    if aconum == 1:
                        aco = True
                    aconum -= 1
                    last.pop()
                else:
                    return False
            elif x == ')':
                if par:
                    return False
                elif last[-1] == 'par':
                    if parnum == 1:
                        par = True
                    parnum -= 1
                    last.pop()
                else:
                    return False
            elif x == ']':
                if bra:
                    return False
                elif last[-1] == 'bra':
                    if branum == 1:
                        bra = True
                    branum -= 1
                    last.pop()
                else:
                    return False
        if parnum == 0 and branum == 0 and aconum == 0:
            return par and bra and aco
        else:
            return False
        