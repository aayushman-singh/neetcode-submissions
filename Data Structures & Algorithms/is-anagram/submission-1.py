class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmap1, hmap2 = {},{}


        for i in range(len(s)):
            hmap1[s[i]] = 1 + hmap1.get(s[i],0)
            hmap2[t[i]] = 1 + hmap2.get(t[i],0)
        return hmap1 == hmap2
