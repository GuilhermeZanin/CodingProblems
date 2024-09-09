def tokenize(expression):
    """Convert the expression into a list of tokens."""
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char in '0123456789':
            num = char
            while i + 1 < len(expression) and expression[i + 1] in '0123456789':
                i += 1
                num += expression[i]
            tokens.append(int(num))
        elif char in '+-*/()' or (char == '*' and i + 1 < len(expression) and expression[i + 1] == '*'):
            if char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
                tokens.append('**')
                i += 1
            else:
                tokens.append(char)
        i += 1
    return tokens

def precedence(op):
    """Return the precedence of the given operator."""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '**':
        return 3
    return 0

def apply_operator(operators, values):
    """Apply an operator to the top two values on the stack."""
    op = operators.pop()
    right = values.pop()
    left = values.pop()
    if op == '+':
        values.append(left + right)
    elif op == '-':
        values.append(left - right)
    elif op == '*':
        values.append(left * right)
    elif op == '/':
        values.append(left // right)
    elif op == '**':
        values.append(left ** right)

def evaluate(expression):
    """Evaluate the given mathematical expression."""
    tokens = tokenize(expression)
    values = []
    operators = []
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if isinstance(token, int):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove '('
        elif token in '+-*/':
            while (operators and operators[-1] in '+-*/' and 
                   precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)
        elif token == '**':
            while (operators and operators[-1] == '**'):
                apply_operator(operators, values)
            operators.append(token)
        
        i += 1
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

# Test cases
print(evaluate("2+(3-1)**3"))  # Output: 512
print(evaluate("(2-0)*(6/2)"))  # Output: 6
print(evaluate("6*(4/2)+3*1"))  # Output: 15
print(evaluate("100*2**4"))      # Output: 1600
