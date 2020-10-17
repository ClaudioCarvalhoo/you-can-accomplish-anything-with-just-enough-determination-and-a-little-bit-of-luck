# O(1)
# len(cells) = 8

from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        states = {}
        states_i = {}

        if N == 0:
            return cells

        for i in range(N):
            if tuple(cells) in states:
                loop_start = states[tuple(cells)]
                loop_end = i
                loop_size = loop_end - loop_start
                to_end = N - i
                return states_i[loop_start + (to_end % loop_size)]
            else:
                states[tuple(cells)] = i
                states_i[i] = cells
                cells = self.nextDay(cells)

        return cells

    def nextDay(self, cells: List[int]) -> List[int]:
        res = [0]
        for i in range(1, len(cells) - 1):
            res.append(1 if cells[i - 1] == cells[i + 1] else 0)
        res.append(0)
        return res