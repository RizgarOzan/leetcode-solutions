// 3. Longest Substring Without Repeating Characters (Medium)
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
//
// Approach: sliding window. Grow the window to the right; when a repeated
// character appears, jump the left edge past its previous position.
// A dictionary remembers the last index of each character.
// O(n) time, O(min(n, alphabet)) space.

using System.Collections.Generic;
using System;

public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        var lastIndex = new Dictionary<char, int>();
        int best = 0;
        int left = 0;
        for (int right = 0; right < s.Length; right++)
        {
            char c = s[right];
            if (lastIndex.TryGetValue(c, out int prev) && prev >= left)
            {
                left = prev + 1;
            }
            lastIndex[c] = right;
            best = Math.Max(best, right - left + 1);
        }
        return best;
    }
}
