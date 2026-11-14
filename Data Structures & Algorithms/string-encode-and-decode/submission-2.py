class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+"#"+strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        result = []
        j = 0 
        lenght = ""

        while  j< len(s):
            
            lenght += s[j]
            j +=1
            if s[j]=="#" : 
                lenght = int(lenght)
                result.append(s[j+1:j+lenght+1]) 
                j = j + lenght+1
                lenght = ""


        return result
