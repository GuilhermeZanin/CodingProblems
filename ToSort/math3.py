import re

# Helper function to define precedence of operators
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '**':
        return 3
    return 0

# Helper function to apply an operator to two numbers
def apply_operator(operands, operator):
    b = operands.pop()  # second operand
    a = operands.pop()  # first operand
    
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a // b  # integer division
    elif operator == '**':
        return a ** b

# Convert infix expression to postfix (Reverse Polish Notation)
def infix_to_postfix(tokens):
    output = []
    operators = []
    
    for token in tokens:
        if token.isdigit():  # If the token is a number, add it to the output
            output.append(int(token))
        elif token == '(':
            operators.append(token)  # Push '(' to operators stack
        elif token == ')':
            # Pop operators until '(' is found
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # remove the '('
        else:
            # Handle exponentiation (**) correctly
            if token == '*' and len(operators) > 0 and operators[-1] == '*':
                token = '**'
                operators.pop()
            
            # Operator: Pop from operator stack if precedence is higher or equal
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                output.append(operators.pop())
            operators.append(token)  # Push current operator
    
    # Pop the remaining operators
    while operators:
        output.append(operators.pop())
    
    return output

# Evaluate a postfix expression (RPN)
def evaluate_postfix(postfix):
    operands = []
    
    for token in postfix:
        if isinstance(token, int):
            operands.append(token)  # push numbers to operands stack
        else:
            # Apply the operator to the top two operands
            operands.append(apply_operator(operands, token))
    
    return operands[0]  # result is the last remaining item in the stack

# Tokenize the expression
def tokenize(expression):
    # Add handling for implicit multiplication, e.g., "2(3)" -> "2*(3)"
    expression = re.sub(r'(\d)\(', r'\1*(', expression)
    expression = re.sub(r'\)(\d)', r')*\1', expression)
    
    # Tokenize numbers, operators, and parentheses
    tokens = re.findall(r'\d+|[-+*/()]|\*\*', expression)
    return tokens

# Main function to evaluate the mathematical expression
def MathChallenge(expression):
    # Step 1: Tokenize the input expression
    tokens = tokenize(expression)
    
    # DEBUG: Print tokens to see if they are tokenized correctly
    print("Tokens:", tokens)
    
    # Step 2: Convert the tokens to postfix notation (RPN)
    postfix = infix_to_postfix(tokens)
    
    # DEBUG: Print postfix to verify if the conversion is correct
    print("Postfix:", postfix)
    
    # Step 3: Evaluate the postfix expression
    result = evaluate_postfix(postfix)
    
    return result

# Test cases to verify the solution
print(MathChallenge("2+(3-1)**3"))  # Expected output: 10
print(MathChallenge("(2-0)(6/2)"))  # Expected output: 6
print(MathChallenge("6(4/2)+3*1"))  # Expected output: 15
print(MathChallenge("100*2**4"))  # Expected output: 1600
