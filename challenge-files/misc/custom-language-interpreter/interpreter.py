#!/usr/bin/env python3
"""Tiny stack-based language interpreter.
Commands:
  PUSH <n>  push number
  ADD SUB MUL  pop a,b push b op a
  DUP  duplicate top
  OUT  pop and print as char
  LOOP <n> ... END  repeat block n times
Example program is in program.txt
"""
def run(code):
    stack = []
    i = 0
    tokens = code.replace('\n',' ').split()
    while i < len(tokens):
        t = tokens[i]
        if t == 'PUSH':
            stack.append(int(tokens[i+1])); i += 2
        elif t == 'ADD':
            b,a = stack.pop(), stack.pop(); stack.append(a+b); i+=1
        elif t == 'SUB':
            b,a = stack.pop(), stack.pop(); stack.append(a-b); i+=1
        elif t == 'MUL':
            b,a = stack.pop(), stack.pop(); stack.append(a*b); i+=1
        elif t == 'DUP':
            stack.append(stack[-1]); i+=1
        elif t == 'OUT':
            print(chr(stack.pop()), end=''); i+=1
        elif t == 'LOOP':
            n = int(tokens[i+1]); end = tokens.index('END', i)
            block = ' '.join(tokens[i+2:end])
            for _ in range(n):
                run(block)
            i = end+1
        else:
            i += 1
    print()

if __name__ == '__main__':
    import sys
    code = open(sys.argv[1]).read()
    run(code)
