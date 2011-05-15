#!/usr/bin/env python
import sys

def decodepubkey(s):
	ret=[]
	o=0
	while o < len(s):
		l = ord(s[o+3])
		ret.append((8*l, s[o+4:o+4+l]))
		o = o + 4 + l
	return tuple(ret)

def tonumber(s):
	i = 0
	for char in s:
		i = i << 8
		i = i | ord(char)
	return i

try:
	sshpubkey, privkeytail = sys.argv[1:]
except:
	print >> sys.stderr, "usage: %s sshpubkey privkeytail" % sys.argv[0]
	sys.exit(1)

print "sshpubkey=%r" % sshpubkey
print "privkeytail=%r" % privkeytail

pubkeybin = sshpubkey.decode('base64')

decoded = decodepubkey(pubkeybin)
keytype = decoded[0][1]

if keytype != "ssh-dss":
	print >> sys.stderr, "wrong keytype"
	sys.exit(1)

p = decoded[1][0], tonumber(decoded[1][1])
q = decoded[2][0], tonumber(decoded[2][1])
g = decoded[3][0], tonumber(decoded[3][1])
y = decoded[4][0], tonumber(decoded[4][1])

print "p=%r" % (p,)
print "q=%r" % (q,)
print "g=%r" % (g,)
print "y=%r" % (y,)

privkeytailbin = privkeytail.decode('base64')
xtail = (len(privkeytailbin)*8, tonumber(privkeytailbin))
print "xtail=%r" % (xtail,)
increment = increment = 1<<xtail[0]
print "increment=%r" % increment
maximum = (q[1]-xtail[1])/increment
print "maximum=%r" % maximum
