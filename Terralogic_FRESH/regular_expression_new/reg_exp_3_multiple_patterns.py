import re
patterns = ["this","that"]
text = "does this text match the pattern 123 456 anil@gmail.com"
for pattern in patterns:
    print "looking for -%s- in -%s-"%(pattern,text)
    if re.search(pattern,text):
        print "pattern match found"
    else:
        print "no match found"