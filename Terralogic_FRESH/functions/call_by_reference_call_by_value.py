# https://www.geeksforgeeks.org/is-python-call-by-reference-or-call-by-value/
# refer above link for the same

# immutable things call by value- int,string, tuple
# mutable things call by reference - list, dict

# call by value
st = "good"
def sample():
    st = "good morning"
    print("inside function",st)

sample()
print("outside  function",st)

# call by reference

def add_more(new_list):
    new_list.append(60)
    print("inside function", new_list)

new_list = [10,20,30,40,50]
add_more(new_list)
print("outside function", new_list)