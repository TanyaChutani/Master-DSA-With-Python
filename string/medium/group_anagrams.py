from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output = defaultdict(list)
        for w in strs:
            final_output["".join(sorted(w))].append(w)
        return final_output.values()
