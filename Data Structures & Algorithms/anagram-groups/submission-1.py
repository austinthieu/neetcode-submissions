class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        result = []
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key].append(s)

        for value in anagrams.values():
            result.append(value)

        return result
