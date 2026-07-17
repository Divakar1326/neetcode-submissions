class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        s_dict = {}

        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        l = 0
        r = 0
        count = 0

        start = 0
        length = float("inf")

        while r < len(s):

            s_dict[s[r]] = s_dict.get(s[r], 0) + 1

            if s[r] in t_dict and s_dict[s[r]] <= t_dict[s[r]]:
                count += 1

            while count == len(t):

                # Update answer
                if r - l + 1 < length:
                    length = r - l + 1
                    start = l

                # Remove unnecessary character
                if s[l] not in t_dict:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                    l += 1

                # Remove extra copy
                elif s_dict[s[l]] > t_dict[s[l]]:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                    l += 1

                # Removing this character makes window invalid
                else:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                    l += 1
                    count -= 1

            r += 1

        if length == float("inf"):
            return ""

        return s[start:start + length]