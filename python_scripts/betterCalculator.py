def tokenize(expression):
    tokens = []
    current_number = ''
    
    for char in expression.replace(' ', ''):
        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                tokens.append(float(current_number))
                current_number = ''
            tokens.append(char)
    
    if current_number:
        tokens.append(float(current_number))
    return tokens

def perform_operation(a, op, b):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b if b != 0 else float('inf')
    elif op == '^': return a ** b
    raise ValueError(f"Unknown operator: {op}")

def calculate(tokens):
    # Handle brackets first
    while '(' in tokens:
        start = -1
        end = -1
        for i, token in enumerate(tokens):
            if token == '(': start = i
            if token == ')':
                end = i
                break
        if start >= 0 and end >= 0:
            sub_result = calculate(tokens[start + 1:end])
            tokens[start:end + 1] = [sub_result]
    
    # Handle exponents
    i = 0
    while i < len(tokens):
        if tokens[i] == '^':
            result = perform_operation(tokens[i-1], '^', tokens[i+1])
            tokens[i-1:i+2] = [result]
            i -= 1
        i += 1
    
    # Handle multiplication and division
    i = 0
    while i < len(tokens):
        if tokens[i] in ['*', '/']:
            result = perform_operation(tokens[i-1], tokens[i], tokens[i+1])
            tokens[i-1:i+2] = [result]
            i -= 1
        i += 1
    
    # Handle addition and subtraction
    i = 0
    while i < len(tokens):
        if tokens[i] in ['+', '-']:
            result = perform_operation(tokens[i-1], tokens[i], tokens[i+1])
            tokens[i-1:i+2] = [result]
            i -= 1
        i += 1
    
    return tokens[0]

def main():
    while True:
        expr = input("Enter expression (or 'q' to quit): ")
        if expr.lower() == 'q':
            break
        try:
            tokens = tokenize(expr)
            result = calculate(tokens)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()