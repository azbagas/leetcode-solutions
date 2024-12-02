from typing import Dict, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map: Dict[str, int] = {}

        # Key: angkanya
        # Value: frekuensinya
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        # Urutkan berdasarkan value
        # key=lambda item: item[1] artinya urutkan berdasarkan value
        sorted_hash_map_by_value = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))

        # Ambil k teratas
        result = []
        i = 1
        for key in sorted_hash_map_by_value.keys():
            if i > k: break
            result.append(key)
            i += 1

        return result
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))