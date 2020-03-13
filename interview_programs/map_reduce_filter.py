def add(num):
    return num + num

a = map(add, [1,2,2])
print(type(a))
print(list(a))


# Python3 program to check for
# balanced parenthesis.

# function to check if
# paranthesis are balanced
def areParanthesisBalanced(expr):
    s = [];
    if len(expr) % 2 == 1:
        return  False

    # Traversing the Expression
    for i in range(len(expr)):

        if (expr[i] == '(' or
                expr[i] == '[' or expr[i] == '{'):
            # Push the element in the stack
            if expr[i] in s:
                return False
            s.append(expr[i]);
            continue;

        # IF current character is not opening
        # bracket, then it must be closing.
        # So stack cannot be empty at this point.
        if (len(s) == 0):
            return False;

        if expr[i] == ')':
            print("a")

            # Store the top element in a
            x = s.pop();

            if (x == '{' or x == '['):
                return False;

        elif expr[i] == '}':
            print("b")

            # Store the top element in b
            x = s.pop();

            if (x == '(' or x == '['):
                return False;

        elif x == ']':
            print("c")

            # Store the top element in c
            x = s.pop();

            if (x == '(' or x == '{'):
                return False;

            # Check Empty Stack
    if len(s):
        return True
    else:
        return False


# Driver Code
if __name__ == "__main__":

    expr = "[{()]]";

    if (areParanthesisBalanced(expr)):
        print("Balanced");
    else:
        print("Not Balanced");

    # This code is contributed by AnkitRai01
