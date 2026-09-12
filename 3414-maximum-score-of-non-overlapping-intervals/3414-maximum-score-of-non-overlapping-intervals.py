class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect

        n = len(intervals)

        arr = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in arr]

        # next[i] = first interval whose start > arr[i].right
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect.bisect_right(starts, arr[i][1])

        # dp[i][k] = best answer using intervals i...n-1
        # with at most k intervals
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, original_index = arr[i]

            for k in range(1, 5):

                # Option 1: skip current interval
                skip = dp[i + 1][k]

                # Option 2: take current interval
                next_score, next_indices = dp[next_idx[i]][k - 1]

                take = (
                    w + next_score,
                    tuple(sorted((original_index,) + next_indices))
                )

                # Maximum score first.
                # If score is equal, lexicographically smaller indices.
                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip)

        return list(dp[0][4][1])
        