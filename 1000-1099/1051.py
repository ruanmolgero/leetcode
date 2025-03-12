class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        aux = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if aux[i] != heights[i]:
                cnt += 1

        return cnt
        