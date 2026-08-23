class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num) // 2
        left = num[:n]
        right = num[n:]

        left_sum = sum(int(c) for c in left if c != '?')
        right_sum = sum(int(c) for c in right if c != '?')

        left_q = left.count('?')
        right_q = right.count('?')

        diff = left_sum - right_sum
        q_diff = left_q - right_q

        if q_diff % 2 != 0:
            return True

        return diff != -9 * q_diff // 2