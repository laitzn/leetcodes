class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_len = 0
        esquerda = 0
        
        for direita, caractere in enumerate(s):
            if caractere in char_map and char_map[caractere] >= esquerda:
                esquerda = char_map[caractere] + 1

            char_map[caractere] = direita

            max_len = max(max_len, direita - esquerda + 1)
            
        return max_len