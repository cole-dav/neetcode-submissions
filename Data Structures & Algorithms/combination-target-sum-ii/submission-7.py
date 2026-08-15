class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        subset = []
        candidates.sort()

        def dfs(i,total):
            if total == target:
                result.add(tuple(subset))
                return
            if total > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1,total + candidates[i])
            subset.pop()

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, total)

        dfs(0,0)
        return [list(combination) for combination in result]