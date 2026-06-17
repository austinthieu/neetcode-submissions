class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            # If its a closing parantheses
            if c in closeToOpen:
                # Check if stack isn't empty and look at top element if its equal to corresponding opening paranthesies
                if stack and stack[-1] == closeToOpen[c]:
                   stack.pop()
                else:
                    return False
            # Add opening parantheses to stack
            else:
                stack.append(c)
        
        ## Only can return true if our stack is empty
        return True if not stack else False