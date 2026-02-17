def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    
    stack = []
    num = 0
    sign = '+'
    
    for i in range(len(expression)):
        char = expression[i]
        
        if char.isdigit():
            num = num * 10 + int(char)
        
        if char in "+-*/" or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(stack.pop() / num)
            
            sign = char
            num = 0
    
    return float(round(sum(stack), 2))


if __name__ == "__main__":
    expr = input("Enter mathematical expression: ")
    result = calculate(expr)
    print("Result:", result)

