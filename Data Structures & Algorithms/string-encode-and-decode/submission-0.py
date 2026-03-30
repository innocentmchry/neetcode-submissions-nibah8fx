class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str_arr = []
        for word in strs:
            new_word = []
            for ch in word:
                new_word.append(chr(ord(ch) + 3))
            
            new_str_arr.append(''.join(new_word))
          
        return str(new_str_arr)

    def decode(self, s: str) -> List[str]:

        s = ast.literal_eval(s)
        new_str_arr = []

        for word in s:
            new_word = []
            for ch in word:
                new_word.append(chr(ord(ch) - 3))
            
            new_str_arr.append(''.join(new_word))
        
        return new_str_arr