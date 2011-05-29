#!/usr/bin/env python
import sys, pari, time

# invoke this script with a chosen range of numbers between 0 and
# data's max

try:
	datafile, inmin, inmax= sys.argv[1:]
except:
	print >> sys.stderr, "usage: %s datafile min max" % sys.argv[0]
	sys.exit(1)

inmin=int(inmin)
inmax=int(inmax)
exec(file(datafile).read())

# farm.py does rough integer division, it may overshoot a bit
if inmax > maximum:
	inmax = maximum
	print >> sys.stderr, "limiting max to %d" % maximum

print >> sys.stderr, "running from %d to %d" % (inmin, inmax)

# start at the chosen minimum
curval = xtail[1]+increment*inmin
# unpack tuples for performance
target = y[1]
gval = g[1]
pval = p[1]
yval = y[1]
for i in xrange(inmax-inmin+1):
    # we should actually calculate pari.Mod() outside of this loop
    # for a 4% win
	if (pari.Mod(gval,pval)**curval)[1] == yval:
		print
		while True:
		    # keep printing it to avoid our tmux window going away
			print 'found %d' % curval
			sys.stdout.flush()
			time.sleep(1)
		sys.exit(0)
	if i % 100000 == 0:
	    # describe some progress
		print '%d%%' % (100 * i / (inmax-inmin+1)), 
		sys.stdout.flush()
	# walk the range
	curval = curval + increment
