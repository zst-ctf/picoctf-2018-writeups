#!/usr/bin/env python3
import socket


def get_total_depth(eq):
    count = 0
    max_count = 0
    for ch in eq:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1

        if count > max_count:
            max_count = count
    return max_count


def simplify(equation):
    items = equation.split(' + ')
    first = items.pop(0)
    second = items.pop(0)

    result = ''

    # Count depth of brackets
    # [absorb] into the deeper item
    # [combine] rule if they are equal
    d1 = get_total_depth(first)
    d2 = get_total_depth(second)
    
    # [absorb] rule - left is deeper
    if d1 > d2:
        result = first[:-1] + second + first[-1]
    
    # [absorb] rule - right is deeper
    elif d2 > d1:
        result = second[0] + first + second[1:]

    # [combine] rule - equal depth
    else:
        result = first + second

    # [left-associative] rule
    if len(items) > 0:
        items.insert(0, result)
        result = ' + '.join(items)

    # print(f"Debug: {equation} -> {result}", )
    return result

    '''
    # OLD METHOD - Produces false positives 

    # *[combine] rule - equal priority
    if first == second:
        result = first + second

    # [absorb] rule - left 3 brackets (higher priority)
    elif first.endswith(')))'):
        print(f"Rule B")
        result = first[:-1] + second + first[-1]

    # [absorb] rule - right 3 brackets (higher priority)
    elif second.startswith('((('):
        print(f"Rule A")
        result = second[0] + first + second[1:]

    # [absorb] rule - left 2 brackets (lower priority)
    elif first.endswith('))'):
        print(f"Rule D")
        result = first[:-1] + second + first[-1]

    # [absorb] rule - right 2 brackets (lower priority)
    elif second.startswith('(('):
        print(f"Rule C")
        result = second[0] + first + second[1:]

    # [combine] rule
    else:
        result = first + second
    '''



def simplify_fully(equation):
    while '+' in equation:
        equation = simplify(equation)
    return equation


def rule_tests():
    '''
    Rules:
    () + () = ()()                                      => [combine]
    ((())) + () = ((())())                              => [absorb-right]
    () + ((())) = (()(()))                              => [absorb-left]
    (())(()) + () = (())(()())                          => [combined-absorb-right]
    () + (())(()) = (()())(())                          => [combined-absorb-left]
    (())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
    ((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
    () + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]
    '''

    # Assert for rules
    assert simplify('() + ()') == '()()'  # => [combine]
    assert simplify('((())) + ()') == '((())())'  # => [absorb-right]
    assert simplify('() + ((()))') == '(()(()))'  # => [absorb-left]
    assert simplify('(())(()) + ()') == '(())(()())'  # => [combined-absorb-right]
    assert simplify('() + (())(())') == '(()())(())'  # => [combined-absorb-left]
    assert simplify('(())(()) + ((()))') == '((())(())(()))'  # => [absorb-combined-right]
    assert simplify('((())) + (())(())') == '((())(())(()))'  # => [absorb-combined-left]
    assert simplify('() + (()) + ((()))') == '(()()) + ((()))'  # => [left-associative]
    assert simplify_fully('() + (()) + ((()))') == '((()())(()))'  # => [left-associative]


def get_equation(data):
    """Get the equation from all the text"""
    for line in data.splitlines()[::-1]:
        if ' = ???' in line:
            return line.split(' = ???')[0]
    return None

def main():
    s = socket.socket()
    s.connect(('2018shell2.picoctf.com', 1542))

    data = ''
    while True:
        data += s.recv(40960).decode().strip()
        if not data:
            continue
        print("<< Received >>", data)

        if '>' in data:
            equation = get_equation(data)
            solution = simplify_fully(equation)

            print("<< Equation:", equation)
            print("<< Solution:", solution, '\n')
            s.send(solution.encode() + b'\n')
            data = ''

        if 'picoCTF{' in data:
            quit()

if __name__ == '__main__':
    # Sample rules
    rule_tests()

    # Extra tests from my failed runs
    assert simplify_fully('(()()) + (()()())') == '(()())(()()())'
    assert simplify_fully('((())()) + ((())())') == '((())())((())())'
    assert simplify_fully('((())()) + ()()() + (())') == '((())()()()()(()))'
    assert simplify_fully('((())()()()()) + (())') == '((())()()()()(()))'
    assert simplify_fully('(()(())) + (()()()) + ((())())') == '(()(())(()()()))((())())'
    assert simplify_fully('(()()) + (()) + (()(()))') == '((()())(())()(()))'
    assert simplify_fully('() + (()()()(())()()) + ((())()) + (()(((()()())()())()())) + (()()()()()()()())') == '((()()()()(())()())((())())()(((()()())()())()())(()()()()()()()()))'

    print("Starting...")
    main()
