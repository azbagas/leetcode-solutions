class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Pakai hash yang nyimpan jumlah huruf
        sBag = {}
        for letter in s:
            if letter not in sBag:
                sBag[letter] = 1
            else:
                sBag[letter] = sBag[letter] + 1
        
        tBag = {}
        for letter in t:
            if letter not in tBag:
                tBag[letter] = 1
            else:
                tBag[letter] = tBag[letter] + 1

        if len(sBag) != len(tBag):
            return False

        unique_letters_count = 0
        for letter in sBag:
            if letter in tBag and tBag[letter] == sBag[letter]:
                unique_letters_count += 1
        
        if len(sBag) == len(tBag) == unique_letters_count:
            return True
        else:
            return False
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaoam"))