# https://leetcode.com/problems/valid-anagram/description/ 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this approach works for unicode also
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        if len(s_map) != len(t_map):
            return False

        # this can be written as return s_map == t_map
        for char in s_map:
            if s_map.get(char, 0) != t_map.get(char, 0):
                return False
        return True
