class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            hash_map = dict.fromkeys(set("".join([s, t])), 0)
            for i, j in zip(s, t):
                hash_map[i] += 1
                hash_map[j] -= 1
            if any(hash_map.values()):
                return False
            else:
                return True
        else:
            return False
