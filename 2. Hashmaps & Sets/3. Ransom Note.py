class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        for char in ransom_count:
            if ransom_count[char] > magazine_count[char]:
                return False
        return True