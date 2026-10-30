from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):

        def solve(start1, dur1, start2, dur2):
            rides = sorted(zip(start2, dur2))

            starts = [s for s, d in rides]

            prefix = []
            mini = float('inf')

            for s, d in rides:
                mini = min(mini, d)
                prefix.append(mini)

            suffix = [0] * len(rides)
            mini = float('inf')

            for i in range(len(rides) - 1, -1, -1):
                s, d = rides[i]
                mini = min(mini, s + d)
                suffix[i] = mini

            ans = float('inf')

            for s, d in zip(start1, dur1):
                finish = s + d
                idx = bisect_right(starts, finish)

                if idx > 0:
                    ans = min(ans, finish + prefix[idx - 1])

                if idx < len(starts):
                    ans = min(ans, suffix[idx])

            return ans

        a = solve(landStartTime, landDuration,
                  waterStartTime, waterDuration)

        b = solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)

        return min(a, b)