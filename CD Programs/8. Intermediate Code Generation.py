OPERATORS = set(['+', '-', '*', '/', '(', ')']) 
PRI = {'+':1, '-':1, '*':2, '/':2} 

def infix_to_postfix(formula): 
    stack = [] 
    output = '' 
    for ch in formula: 
        if ch not in OPERATORS: 
            output += ch 
        elif ch == '(': 
            stack.append('(') 
        elif ch == ')': 
            while stack and stack[-1] != '(': 
                output += stack.pop() 
            stack.pop() 
        else: 
            while stack and stack[-1] != '(' and PRI[ch] <= PRI[stack[-1]]: 
                output += stack.pop() 
            stack.append(ch)  
    while stack: 
        output += stack.pop() 
    print(f'POSTFIX: {output}') 
    return output

def generate3AC(pos): 
    print("### THREE ADDRESS CODE GENERATION ###") 
    exp_stack = [] 
    t = 1 

    for i in pos: 
        if i not in OPERATORS: 
            exp_stack.append(i) 
        else: 
            print(f't{t} := {exp_stack[-2]} {i} {exp_stack[-1]}') 
            exp_stack=exp_stack[:-2] 
            exp_stack.append(f't{t}') 
            t+=1 
expres = input("INPUT THE EXPRESSION: ") 
pos = infix_to_postfix(expres) 
generate3AC(pos)

## input : a=3+4*(8-7*(c-b)+2)






Sample Input and Output: 
INPUT THE EXPRESSION: a=3+4*(8-7*(c-b)+2) 
POSTFIX: a=3487cb-*-2+*+ 
### THREE ADDRESS CODE GENERATION ### 
t1 := c - b 
t2 := 7 * t1 
t3 := 8 - t2 
t4 := t3 + 2 
t5 := 4 * t4 
t6 := 3 + t5 