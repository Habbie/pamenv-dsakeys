#!/usr/bin/env python
import sys

# the output of this script is a suitable datafile for farm.py and force.py

# ssh pubkeys are a pretty straightforward length-value encoding
# kinda Pascal-string like.
def decodepubkey(s):
	ret=[]
	o=0
	while o < len(s):
	    # hack: assume we can ignore the top 3 bytes of the length field
		l = ord(s[o+3])
		# grab value, include size in bits
		ret.append((8*l, s[o+4:o+4+l]))
		# skip to next pair
		o = o + 4 + l
	return tuple(ret)

# turn a binary string in network order into a (long) integer
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

# grab the public variables from the decoded pubkey,
# including their length in bits
p = decoded[1][0], tonumber(decoded[1][1])
q = decoded[2][0], tonumber(decoded[2][1])
g = decoded[3][0], tonumber(decoded[3][1])
y = decoded[4][0], tonumber(decoded[4][1])

# dump them out
print "p=%r" % (p,)
print "q=%r" % (q,)
print "g=%r" % (g,)
print "y=%r" % (y,)

privkeytailbin = privkeytail.decode('base64')

# make sure we save the length, it could save us a lot of 
# brute forcing time
xtail = (len(privkeytailbin)*8, tonumber(privkeytailbin))
print "xtail=%r" % (xtail,)

# calculate the increment that will, when iterating from
# xtail to q, should hit our desired x
increment = increment = 1<<xtail[0]
print "increment=%r" % increment

# calculate the total forcing range
maximum = (q[1]-xtail[1])/increment
print "maximum=%r" % maximum
