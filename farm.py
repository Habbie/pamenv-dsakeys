#!/usr/bin/env python
import sys, os

datafile = sys.argv[1]
weight = int(sys.argv[2])
hosts = sys.argv[3:]
if not hosts:
	print >> sys.stderr, "usage: %s datafile weight host1 [host2 ..]" % sys.argv[0]
	sys.exit(1)

exec(file(datafile).read())

print 'Distributing data..'
for h in hosts:
	os.system("scp data %s:" % h)

print 'Farming out work..'
size = maximum / weight / len(hosts) +1
base = 0
os.system("tmux new-session -d")
os.system("tmux set-option set-remain-on-exit on")
for h in hosts:
	for i in range(weight):
		os.system("tmux split-window -h 'ssh %s ./force.py data %d %d'" % (h, base, base+size))
		os.system("tmux select-layout tiled")
		base = base + size

