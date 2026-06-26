class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stringX = str(x)

        invertidoX = stringX[::-1]

        return stringX == invertidoX