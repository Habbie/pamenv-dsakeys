#!/usr/bin/env python
import sys, pari

from pyasn1.type.univ import Sequence, Integer
from pyasn1.codec.der import encoder

try:
	datafile = sys.argv[1]
	x = sys.argv[2]
except:
	print >> sys.stderr, "usage: %s datafile x" % sys.argv[0]
	sys.exit(1)

exec(file(datafile).read())

sys.stdout.write(encoder.encode(
	Sequence().
		setComponentByPosition(0, Integer('0')).
		setComponentByPosition(1, Integer(p[1])).
		setComponentByPosition(2, Integer(q[1])).
		setComponentByPosition(3, Integer(g[1])).
		setComponentByPosition(4, Integer(y[1])).
		setComponentByPosition(5, Integer(x)), ''))
