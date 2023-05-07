"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

s = "()"

opening = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

closing = {
            ')': '(',
            '}': '{',
            ']': '['
        }

print(opening)

stack = []
def check_paranthesis(s):
    for each in s:
        print(each)
        if each not in opening and each not in closing:
            return False
        if not stack or (stack[-1] in opening and each in closing):
            stack.append(each)
            print(stack)
            continue
        if each in closing:
            if closing[each] == stack[-1]:
                del stack[-1]
            else:
                return False
    return len(stack) == 0

f = ['(','{',"["]
def check_p(st):
    st = []
    for i in s:
        if i in f:
            st.append(i)
        else:
            if len(st) == 0:
                return False
            elif i == ')' and st[-1] == '(':
                st.pop()
            elif i == '}' and st[-1] == '{':
                st.pop()
            elif i == ']' and st[-1] == '[':
                st.pop()
            else:
                return False
    return len(st) == 0

print(check_p(s))