class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        for char in strs :
            count_key = [0]*26
            for c in char :
                count_key[ord(c)-ord('a')]+=1
            
            result[tuple(count_key)].append(char)

        return list(result.values())
