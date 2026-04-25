gram = { 
"S": ["(L)", "a"], 
"L": ["L,S", "S"] 
} 
start = "S" 
inp = "((a,a),(a,a))$" 
stack = "$" 
print(f'{"stack":<20}|{"Input Buffer":<20}|Parsing Action') 
print("-" * 60) 
while True: 
    reduced = False 
    for lhs in gram: 
        for rhs in gram[lhs]: 
            if rhs in stack: 
            
                            stack = stack.replace(rhs, lhs, 1) 
                            print(f'{stack:<20}|{inp:<20}|Reduce {lhs}->{rhs}') 
                            reduced = True 
                            break 
        if reduced: 
            break 
            
    if not reduced: 
        stack += inp[0] 
        inp = inp[1:] 
        print(f'{stack:<20}|{inp:<20}|Shift') 
    if stack == "$S" and inp == "$": 
        print(f'{stack:<20}|{inp:<20}|Accepted') 
        break 
    if inp == "" and not reduced: 
        print(f'{stack:<20}|{inp:<20}|Rejected') 
        break   