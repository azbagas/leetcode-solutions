from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Inital empty groups
        groups: Dict[str, List[str]] = {}

        for word in strs:
            # Sort the word
            sorted_str = ''.join(sorted(word))
            if sorted_str in groups:
                groups[sorted_str].append(word)
            else:
                groups[sorted_str] = [word]

        return list(groups.values())
        
if __name__ == "__main__":
    solution = Solution()
    # print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(solution.groupAnagrams([""]))