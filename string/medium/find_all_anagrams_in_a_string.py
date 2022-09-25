class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        phash = (dict.fromkeys(p+s, 0))
        shash = (dict.fromkeys(p+s, 0))
        final_result = []
        
        for i in p:
            phash[i] += 1

        for i in s[:len(p)]:
            shash[i] += 1
        if phash == shash:
            final_result.append(0)
            
        for idx, j in enumerate(s[1:-(len(p)-1) if len(p)!=1 else len(s)]):
            shash[s[idx]]-=1
            shash[s[idx+len(p)]]+=1
            if phash == shash:
                final_result.append(idx+1)
        return final_result
