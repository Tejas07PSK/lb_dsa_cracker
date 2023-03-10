from collections import deque
class Solution:
    def floodFill (self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q, r, c = deque(), len(image), len(image[0])
        q.append((sr, sc))
        while (q):
            i, j = q.popleft()
            if (image[i][j] == color): continue
            if (((i - 1) >= 0) and (image[i][j] == image[i - 1][j])): q.append((i - 1, j))
            if (((i + 1) < r) and (image[i][j] == image[i + 1][j])): q.append((i + 1, j))
            if (((j - 1) >= 0) and (image[i][j] == image[i][j - 1])): q.append((i, j - 1))
            if (((j + 1) < c) and (image[i][j] == image[i][j + 1])): q.append((i, j + 1))
            image[i][j] = color
        return image
