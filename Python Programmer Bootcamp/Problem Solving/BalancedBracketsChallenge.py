def balanced_brackets(input_brackets):
    stack = [0]

    if len(input_brackets) == 0:
        return True

    if ((input_brackets[0] == "}") or
            (input_brackets[0] == "]") or
            (input_brackets[0] == ">") or
            (input_brackets[0] == ")")):
        return False

    for i in range(len(input_brackets)):
        if (input_brackets[i] == "{" or
            input_brackets[i] == "}" or
            input_brackets[i] == ")" or
            input_brackets[i] == "(" or
            input_brackets[i] == "[" or
            input_brackets[i] == "]" or
            input_brackets[i] == ">" or
            input_brackets[i] == "<"):
            stack.append(input_brackets[i])
        if ((stack[-1] == "}" and stack[-2] == "{") or
                (stack[-1] == "]" and stack[-2] == "[") or
                (stack[-1] == ")" and stack[-2] == "(") or
                (stack[-1] == ">" and stack[-2] == "<")):
            stack.pop()
            stack.pop()
    return len(stack) == 1

test_cases1 = [
    # Balanced
    ";alkjsdf",             # empty string is balanced
    "(*^*^&^%$$^#%$$#@$#!~##@$#%#%$^%&%:::&*^*&%$^%#^$#)",
    "[]",
    "{}",
    "(())",
    "[[]]",
    "{{}}",
    "([])",
    "{[()]}",
    "((()))",
    "[{()}([])]",
    "(([]){})",
    "{[([]{})]}",          # nested and mixed
    "()[{}]([])",          # multiple groups
    "(((([[[{{{}}}]]]]))))", # deep nesting

    # Not Balanced
    "(",
    ")",
    ")(",
    "([)]",                # wrong order
    "{[(])}",              # wrong nesting
    "((()",                # too many opens
    "(()))",               # too many closes
    "[[[]",                # one missing close
    "[]]]",                # too many closes
    "{[}]",                # mismatched close
    "(([]){)",             # last mismatch
    "[{(()}]])",           # subtle mismatch
]


for j in test_cases1:
    print(f"\nThis is the string: {j}\nEvaluation: {balanced_brackets(j)}")

test_cases2 = [
    # Balanced
    "",                            # empty
    "()",
    "[abc]",
    "{123}",
    "(a+b)*(c-d)",
    "[{()}]42",
    "user(id[0])",
    "{[()]_valid}",
    "func_call(param1[2]{x})",
    "((data[3]+val){check})",
    "x = ({y:[z]})",               # code-like
    "(([]){})--done!",

    # Not Balanced
    "(",
    "([)]",
    "test(123",
    "abc[)]",
    "{key: [value])}",             # mismatch
    "(()))value",
    "(((abc]",
    "user(id[0]",
    "no{end])",
    "[start*(finish})",
    "wrong<>{}",                   # includes angle brackets
    "{name:[data](extra}",         # subtle mis-nesting
]

for k in test_cases2:
    print(f"\nThis is the string: {k}\nEvaluation: {balanced_brackets(k)}")
print(balanced_brackets("))"))