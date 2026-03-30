class Solution:
    def countBits(self, n: int) -> List[int]:
        # Many things to learn here. To calculate bit length of any int n
        # You can use n.bit_length()
        # You can also use bin(n) - 2, since 0x is appended at the start
        # You can also use the formula log2(n) + 1, but you need to handle n=0 separately

        res = []

        for i in range(n+1):
            count = 0
            for j in range(i.bit_length()):
                if (1 << j) & i:
                    count += 1
            
            res.append(count)

        return res