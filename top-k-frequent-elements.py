class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary.update({num: 1})

        return sorted(dictionary.keys(), key=lambda k: -dictionary[k])[:k]
