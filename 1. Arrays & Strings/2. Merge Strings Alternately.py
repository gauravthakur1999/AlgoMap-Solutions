class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        n = max(w1,w2)
        i=0
        res = ""
        while i < n:
            if i < w1:
                res = res + str(word1[i]) 
            if i < w2:
                res = res + str(word2[i])
            i += 1
        return res