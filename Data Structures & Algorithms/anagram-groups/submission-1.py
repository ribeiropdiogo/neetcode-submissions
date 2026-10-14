class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1

            if str(count) in anagrams:
                anagrams[str(count)].append(s)
            else:
                anagrams[str(count)] = [s]
        
        return list(anagrams.values())
        