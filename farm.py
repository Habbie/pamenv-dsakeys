#!/usr/bin/env python
# this script farms out force.py work to remote hosts
import sys, os

# it assumes this datafile is available on the same (relative, if you like)
# path on every host
datafile = sys.argv[1]
# weight tells farm.py how many instances to start on each machine
# a better tool than this would allow you to configure this per host
weight = int(sys.argv[2])
hosts = sys.argv[3:]
if not hosts:
	print >> sys.stderr, "usage: %s datafile weight host1 [host2 ..]" % sys.argv[0]
	sys.exit(1)

# read datafile, assume it's valid Python syntax
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
		# if we don't reset the layout after every few spawns
		# tmux will soon complain that the window we're trying to split
		# is already too small
		os.system("tmux select-layout tiled")
		base = base + size

# try tmux attach after this, then wait for one of the panes
# to say 'found xxx'