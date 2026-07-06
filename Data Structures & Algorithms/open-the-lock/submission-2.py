class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        q = deque([["0000", 0]])
        visited = set()

        while q:
            code, turns = q.popleft()
            
            next_codes = []
            for i in range(len(code)):
                next_codes.append(code[:i] + str((int(code[i]) + 1) % 10) + code[i + 1:])
                next_codes.append(code[:i] + str((int(code[i]) - 1) % 10) + code[i + 1:])
            
            for next_code in next_codes:
                if next_code == target:
                    return turns + 1
                if next_code not in deadends and next_code not in visited:
                    q.append([next_code, turns + 1])
                    visited.add(next_code)
        
        return -1