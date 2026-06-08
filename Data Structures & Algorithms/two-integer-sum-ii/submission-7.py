class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            sum = numbers[rp] + numbers[lp]

            if sum == target:
                return [lp + 1, rp + 1]
            
            if sum < target:
                lp += 1

            if sum > target:
                rp -= 1
    