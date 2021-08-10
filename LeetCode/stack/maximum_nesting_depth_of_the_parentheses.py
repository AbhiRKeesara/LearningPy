class Solution:
    def maxDepth(self, s: str) -> int:

        depth_of_string = 0
        stack = []
        for token in s:
            if token == "(":
                stack.append(token)
                length_of_stack = len(stack)
                depth_of_string = max(depth_of_string, length_of_stack)
            elif token == ")":
                stack.pop()

        return depth_of_string


sol = Solution()

print(sol.maxDepth("()(()())"))
