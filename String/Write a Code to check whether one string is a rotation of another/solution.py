class Solution:
    def rotateString (self, s: str, goal: str) -> bool:
        if (len(s) != len(goal)):
            return False
        return True if goal in (s + s) else False
