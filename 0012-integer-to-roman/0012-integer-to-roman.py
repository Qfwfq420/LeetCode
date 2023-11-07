class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        out = ''
        n = []
        for i in str(num):
            n.append(int(i))
        n.reverse()
        d = 1
        for i in n:
            if i == 4 or i == 9:
                out = roman[d] + roman[(i +1) * d] + out
            elif i >= 5:
                out = roman[d*5] + roman[d] * (i - 5) + out
            else:
               out = roman[d] * i + out
            d *= 10
        return out

        