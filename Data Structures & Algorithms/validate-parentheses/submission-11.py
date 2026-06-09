class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []

        p_dict = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        for p in s:
            if p in p_dict:
                if not p_stack or p_stack[-1] != p_dict[p]:
                    return False
                else:
                    p_stack.pop()
            else:
                p_stack.append(p)

        return not p_stack