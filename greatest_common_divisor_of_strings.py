# 
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_1 = len(str1)
        len_2 = len(str2)

        if len_1 > len_2:
            max_str = str1
            min_str = str2
        else:
            max_str = str2
            min_str = str1

        str_1_map = set(str1)
        str_2_map = set(str2)

        import math
        gcd = math.gcd(len_1, len_2)

        if str1[0:gcd] == str2[0:gcd]:
            if str_1_map ^ str_2_map:
                return ""
            # for key in str_1_map:
            #     if key not in str_2_map:
            #         return ""
            # for key in str_2_map:
            #     if key not in str_1_map:
            #         return ""

            val = str1[0:gcd]
            f1 = False
            while len(val) <= len(max_str):
                if val == max_str:
                    f1 = True
                    break
                val += str1[0:gcd]
            
            val = str1[0:gcd]
            f2 = False
            while len(val) <= len(min_str):
                if val == min_str:
                    f2 = True
                val += str1[0:gcd]
            if f1 and f2:
                return str1[0:gcd]
            
        return ""
