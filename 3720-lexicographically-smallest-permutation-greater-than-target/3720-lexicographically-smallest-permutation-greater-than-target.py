class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            if cnt[t] > 0:
                cnt[t] -= 1
                ans.append(target[i])
            else:
                for j in range(t + 1, 26):
                    if cnt[j] > 0:
                        cnt[j] -= 1
                        ans.append(chr(j + ord('a')))

                        for k in range(26):
                            ans.extend([chr(k + ord('a'))] * cnt[k])

                        return ''.join(ans)
                break

        for i in range(len(ans) - 1, -1, -1):
            cnt[ord(ans[i]) - ord('a')] += 1

            t = ord(target[i]) - ord('a')

            for j in range(t + 1, 26):
                if cnt[j] > 0:
                    result = ans[:i]
                    result.append(chr(j + ord('a')))
                    cnt[j] -= 1

                    for k in range(26):
                        result.extend([chr(k + ord('a'))] * cnt[k])

                    return ''.join(result)

        return ""
        