class Solution(object):
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        i = 0
        n = len(s)
        sign = 1
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            result = result * 10 + digit
            
            if sign * result < INT_MIN:
                return INT_MIN
            if sign * result > INT_MAX:
                return INT_MAX
                
            i += 1
            
        return sign * result