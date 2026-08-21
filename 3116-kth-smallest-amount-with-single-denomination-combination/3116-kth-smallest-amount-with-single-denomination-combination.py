class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd

        def lcm(a, b):
            return a // gcd(a, b) * b

        coins = list(set(coins))

        def count(x):
            total = 0
            m = len(coins)

            for mask in range(1, 1 << m):
                v = 1
                bits = 0
                valid = True

                for i in range(m):
                    if mask >> i & 1:
                        v = lcm(v, coins[i])

                        if v > x:
                            valid = False
                            break

                        bits += 1

                if valid:
                    if bits % 2:
                        total += x // v
                    else:
                        total -= x // v

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
          