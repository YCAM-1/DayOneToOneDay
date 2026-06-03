class Solution:
    def palindrome(self, num):
        s = str(num)
        reversed_s = s[::-1]
        if reversed_s == s:
            return True
        else:
            return False