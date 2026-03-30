class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = collections.deque()
        if tokens is None:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])

        s.append(tokens[0])
        oprd1 = 0
        oprd2 = 0

        res = 0
        for i in range(1, len(tokens)):
            curr = tokens[i]
            if curr == "+":
                oprd2 = int(s.pop())
                oprd1 = int(s.pop())         
                res = oprd1 + oprd2
                s.append(res)
            elif curr == "-":
                oprd2 = int(s.pop())
                oprd1 = int(s.pop())  
                res = oprd1 - oprd2
                s.append(res)
            elif curr == "*":
                oprd2 = int(s.pop())
                oprd1 = int(s.pop())
                res = oprd1 * oprd2
                s.append(res)
            elif curr == "/":
                oprd2 = int(s.pop())
                oprd1 = int(s.pop())
                res = oprd1 / oprd2
                s.append(int(res))
            else:
                s.append(tokens[i])

        return s.pop()


        


        