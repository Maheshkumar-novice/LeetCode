# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_parans = {')': '(', ']': '[', '}': '{'}
        for paran in s:
            if paran not in close_parans:
                stack.append(paran)
                continue
            elif not stack:
                return False
            elif stack.pop() != close_parans[paran]:
                return False
        return not stack
