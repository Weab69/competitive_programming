class Solution:    
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        
        s_list = list(s)

        
        while start < end:
            
            while start < len(s) and not s_list[start] in vowels:
                start += 1

            
            while end >= 0 and not s_list[end] in vowels:
                end -= 1

            
            if start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]                
                start += 1
                end -= 1

        return ''.join(s_list)
