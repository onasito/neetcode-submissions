class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have, need = 0, len(count_t)
        result = ""
        min_len = float("infinity")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in count_t and window[char] == count_t[char]:
                have += 1

            while have == need:
                # update result if this window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    result = s[left:right+1]

                # shrink from left
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1

        return result