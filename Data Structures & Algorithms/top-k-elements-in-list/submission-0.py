class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1

        L = [[] for _ in range(len(nums) + 1)]

        for key, value in hashmap.items():
            L[value].append(key)

        result = []

        for i in range(len(L) - 1, 0, -1):
            for num in L[i]:
                result.append(num)

                if len(result) == k:
                    return result