class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set()
        for d in deadends:
            visited.add(d)
        def children(lock):
            res = []
            for i in range(4):
                #incrementing
                new = lock[:i] + str((int(lock[i]) +1) % 10) + lock[i+1:]
                res.append(new)
                #decrementing
                new = lock[:i] + str((int(lock[i]) +9) % 10) + lock[i+1:]
                res.append(new)
            return res

        visited.add("0000")

        q = deque([("0000", 0)])
        while q:
            current, level = q.popleft()
            if current == target:
                return level
            for c in children(current):
                if c not in visited:
                    q.append((c, level + 1))
                    visited.add(c)
        return -1

        