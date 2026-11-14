class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs :
            word_s = "".join(sorted(word))
            if word_s in hashmap :
                hashmap[word_s].append(word)
            else : hashmap[word_s]=[word]
        return list(hashmap.values())


        