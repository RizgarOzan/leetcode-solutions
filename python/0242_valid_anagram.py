# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
#
# Approach: count letters. Two strings of different length can never be
# anagrams, so bail out early. Otherwise tally every character of the first
# string and subtract the second one; if any count drops below zero the
# strings differ. O(n) time, O(1) space since the alphabet is fixed.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True
