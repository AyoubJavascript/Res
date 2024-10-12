class Solution(object):
    def longestPalindrome(self, s):

        if len(s) == 1 : return s

        def is_palindrom(str):
            return str == str[::-1]

        result = ""

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if is_palindrom(s[i:j+1]):
                    result = s[i:j+1] if len(s[i:j+1]) > len(result) else result
        return result




sol = Solution()
print(sol.longestPalindrome("papapapapaplolololololol"))


