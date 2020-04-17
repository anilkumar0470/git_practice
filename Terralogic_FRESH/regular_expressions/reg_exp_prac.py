import re
pattern = 'this'
text = 'does this text match the this pattern?'
ma = re.search(pattern,text)
s = ma.start()
e = ma.end()
print 'found "%s" in "%s" from %d to %d ("%s")' % \
      (ma.re.pattern,ma.string,s,e,text[s:e])
#print "found %s in %s from %d to %d (%s)" % \
#      (ma.re.pattern,ma.string,s,e,text[s:e])

