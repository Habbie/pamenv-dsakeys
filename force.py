#!/usr/bin/env python
import sys, pari, time

try:
	datafile, inmin, inmax= sys.argv[1:]
except:
	print >> sys.stderr, "usage: %s datafile min max" % sys.argv[0]
	sys.exit(1)

inmin=int(inmin)
inmax=int(inmax)
exec(file(datafile).read())

if inmax > maximum:
	inmax = maximum
	print >> sys.stderr, "limiting max to %d" % maximum

print >> sys.stderr, "running from %d to %d" % (inmin, inmax)

curval = xtail[1]+increment*inmin
target = y[1]
gval = g[1]
pval = p[1]
yval = y[1]
for i in xrange(inmax-inmin+1):
	if (pari.Mod(gval,pval)**curval)[1] == yval:
		print
		while True:
			print 'found %d' % curval
			sys.stdout.flush()
			time.sleep(1)
		sys.exit(0)
	if i % 100000 == 0:
		print '%d%%' % (100 * i / (inmax-inmin+1)), 
		sys.stdout.flush()
	curval = curval + increment
