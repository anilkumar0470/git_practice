
st = "anil kumar pathapati "
l = len(st)
str =""
while l>0:
    str = str +st[l-1]
    l = l - 1
print "hello",str




str = "anil kumar pathapati"
each_word = str.split()
res_str = ''
for word in each_word:
    st =''
    l = len(word)
    while l > 0:
        st = st + word[l - 1]
        l = l- 1
    res_str = res_str +' '+ st
print res_str