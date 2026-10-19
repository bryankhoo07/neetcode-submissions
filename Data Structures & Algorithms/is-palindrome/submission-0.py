class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = re.sub(r'[^a-z0-9]', '', s.lower())
        letters = list(result)

        left = 0
        right = len(letters) - 1

        while left < right:
            if letters[left] != letters[right]:
                return False

            left += 1
            right -= 1
        return True
       