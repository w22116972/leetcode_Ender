class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        # zip(*list) 可以iterate多個集合
        for index, char_group in enumerate(zip(*strs)):
            # 用set和len來檢測char之間是否彼此相同
            if len(set(char_group)) > 1:  
                return strs[0][:index]
        # 此時有兩種可能: 1. 最小長度的先走完 2. 全部都相同長度一起走完
        return min(strs)  # 回傳長度最小的str 


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["aa", "a"]))
