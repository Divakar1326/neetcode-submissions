class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()

                box = (r // 3) * 3 + (c // 3)
                if box not in boxes:
                    boxes[box] = set()

                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True