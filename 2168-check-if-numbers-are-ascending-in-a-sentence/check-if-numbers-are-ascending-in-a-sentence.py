class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1

        for token in s.split():
            if token.isdigit():
                curr = int(token)
                if curr <= prev:
                    return False
                prev = curr
                
        return True