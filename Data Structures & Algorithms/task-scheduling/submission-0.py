from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = Counter(tasks)

        max_freq = max(a.values())
        count_max = sum(1 for v in a.values() if v == max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + count_max
        )