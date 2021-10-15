import re
patterns = ["this","that"]
text = "does this text match the pattern 123 456 anil@gmail.com"
for pattern in patterns:
    print ("looking for {} in {}".format(pattern,text))
    print("looking for ", pattern, "in", text)
    if re.search(pattern,text):
        print ("pattern match found")
    else:
        print ("no match found")