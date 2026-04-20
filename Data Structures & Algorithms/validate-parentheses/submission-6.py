class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch not in {'}', ']', ')'}:
                stack.append(ch)
            else:
                if stack:
                    top = stack.pop()
                    if ch == '}':
                        if top != '{':
                            return False

                    if ch == ']':
                        if top != '[':
                            return False
                    
                    if ch == ')':
                        if top != '(':
                            return False
                else:
                    return False

        return True if len(stack) == 0 else False