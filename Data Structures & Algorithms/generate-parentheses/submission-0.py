class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        cur = []

        def generate(openN, closeN):
            if openN == closeN == n:
                res.append(str(''.join(cur)))
                return

            if openN < n:
                cur.append("(")
                generate(openN + 1, closeN)
                cur.pop()

            if closeN < openN:
                cur.append(")")
                generate(openN, 1 + closeN)
                cur.pop()

        generate(0,0)
        return res