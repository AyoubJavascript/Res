class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # Remove leading and trailing whitespaces
        if not s:
            return 0  # Return 0 if the string is empty after stripping

        sign = 1  # 1 for positive, -1 for negative
        result = 0
        i = 0

        # Handle optional sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Convert the string to integer
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # Clamp the result to fit within the 32-bit signed integer range
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result


# Example usage
sol = Solution()
print(sol.myAtoi("-042"))  # Output: -42
