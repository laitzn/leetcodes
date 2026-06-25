class Solution(object):
    def twoSum(self, nums, target):
        mapa = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in mapa:
                return [mapa[complemento], i]

            mapa[num] = i
        