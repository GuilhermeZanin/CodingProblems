import ast
import operator

# Dictionary of operators to their corresponding functions
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}

def evaluate_expr(node):
    """Recursively evaluate the AST nodes."""
    if isinstance(node, ast.Expression):
        return evaluate_expr(node.body)
    elif isinstance(node, ast.BinOp):
        left = evaluate_expr(node.left)
        right = evaluate_expr(node.right)
        op = operators[type(node.op)]
        return op(left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate_expr(node.operand)
        op = operators[type(node.op)]
        return op(operand)
    elif isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Call):
        func = evaluate_expr(node.func)
        args = [evaluate_expr(arg) for arg in node.args]
        return func(*args)
    else:
        raise TypeError(node)
    
def math_challenge(expr):
    """Evaluate the given mathematical expression safely."""
    # Parse the expression into an AST
    tree = ast.parse(expr, mode='eval')
    # Evaluate the AST and return the result
    return evaluate_expr(tree.body)

# Test cases
print(math_challenge("2+(3-1)**3"))  # Output: 512
print(math_challenge("(2-0)*(6/2)"))  # Output: 6
print(math_challenge("6*(4/2)+3*1"))  # Output: 15
print(math_challenge("100*2**4"))      # Output: 1600
