class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter the alphanum and lowercase it
        s = ''.join(c for c in s if c.isalnum()).lower()
        
        # Check the palindrome
        return s == s[::-1]

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # Filter the alphanum and lowercase it
#         s = ''.join(c for c in s if c.isalnum()).lower()
        
#         # Check the palindrome
#         s_length = len(s)
#         for i in range(s_length//2):
#             if (s[i] != s[s_length - (i + 1)]):
#                 return False
        
#         return True
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))