# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        mi = 0
        mx = 0
        l = max(0, mx - mi)
        se = set()
        for i, c in enumerate(s):
            if c in se or i + 1 == len(s):
                l = max(l, (mx - mi) + 1)
                mx = i
                print(c, mi, mx, l)
                for i, k in enumerate(s[mi:mx], mi):
                    if c == k and k in se:
                        mi = i + 1
                        print(k, mi)
                continue
            mx = i
            se.add(c)
        return max(l, (mx - mi) + 1)
