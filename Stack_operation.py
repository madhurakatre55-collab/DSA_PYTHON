class Stack:
    def __init__(self):
        self.arr = []

    def push(self,x):
        self.arr.append(x)

    def pop(self):
        if self.arr:
            return self.arr.pop()
        return None

    def peek(self):
        if self.arr:
            return self.arr[-1]
        return None

    def display(self):
        print("stack",self.arr)


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    output = []

    for char in expression:
        if char.isspace():
            continue
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()
        elif char in precedence:
            while (
                stack
                and stack[-1] != '('
                and precedence[char] <= precedence[stack[-1]]
            ):
                output.append(stack.pop())
            stack.append(char)
        else:
            raise ValueError(f"Unsupported character: {char}")

    if '(' in stack:
        raise ValueError("Mismatched parentheses")
    while stack:
        output.append(stack.pop())
    return "".join(output)


if __name__ == "__main__":
    print("Postfix:", infix_to_postfix("A+B*C-D"))