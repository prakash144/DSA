class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # hashMap for charCount and anagram
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord("a")] += 1

            # list can't be key of map in python
            res[tuple(count)].append(s)

        return res.values()