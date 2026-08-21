class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        m = c.most_common(k)
        out = []
        for i in m:
            out.append(i[0])
        return out