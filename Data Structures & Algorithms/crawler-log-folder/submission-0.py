class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l == "./":
                continue
            if l == "../" and not stack:
                continue
            elif l == "../":
                stack.pop()
            else:
                stack.append(l)
        
        return len(stack)