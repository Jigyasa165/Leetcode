class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        a = []
        b = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a.append((i, j))
                if img2[i][j] == 1:
                    b.append((i, j))

        count = {}

        for x1, y1 in a:
            for x2, y2 in b:
                shift = (x2 - x1, y2 - y1)
                count[shift] = count.get(shift, 0) + 1

        return max(count.values(), default=0)
        