# 20. Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
#
# Approach: stack. Push opening brackets, pop and match on closing ones.
# The string is valid if every close matches the latest open and the
# stack is empty at the end. O(n) time, O(n) space.

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
