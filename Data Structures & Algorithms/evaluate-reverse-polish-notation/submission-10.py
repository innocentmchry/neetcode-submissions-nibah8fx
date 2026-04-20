class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                opr1 = stack.pop()
                opr2 = stack.pop()
                res = opr2 + opr1
                stack.append(res)
            elif tokens[i] == "*":
                opr1 = stack.pop()
                opr2 = stack.pop()
                res = opr2 * opr1
                stack.append(res)
            elif tokens[i] == "/":
                opr1 = stack.pop()
                opr2 = stack.pop()
                res = opr2 / opr1
                stack.append(int(res))
            elif tokens[i] == "-":
                opr1 = stack.pop()
                opr2 = stack.pop()
                res = opr2 - opr1
                stack.append(res)
            else:
                stack.append(int(tokens[i]))

        return stack.pop()