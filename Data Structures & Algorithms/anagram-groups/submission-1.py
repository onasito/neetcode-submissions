class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedKeys = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in sortedKeys:
                sortedKeys[key] = []
            
            sortedKeys[key].append(word)

        return list(sortedKeys.values())