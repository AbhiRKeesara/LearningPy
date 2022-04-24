class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        opened_paranthesis_count = 0
        for token in s:
            if token == "(" and opened_paranthesis_count > 0:
                stack.append(token)
            if token == ")" and opened_paranthesis_count > 1:
                stack.append(token)
            if token == "(":
                opened_paranthesis_count += 1
            else:
                opened_paranthesis_count -= 1
        return " ".join(stack)


sol = Solution()

print(sol.removeOuterParentheses("(()())(())"))
