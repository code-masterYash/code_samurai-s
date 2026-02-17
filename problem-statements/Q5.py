def calculate(expression):
    expression = expression.replace(" ", "")
    
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(expression):
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
    
    return round(sum(stack), 2)


