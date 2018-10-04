import fabric.api as fabi
import fabric.operations as fop
from hosts import *
import time

fabi.env.key_filename = '~/.ssh/cluster_2018_9_10'

fabi.env.skip_bad_hosts = True
fabi.env.warn_only = True
fabi.env.abort_on_prompts=True

#@fabi.parallel
def runCommand(command):
	"""run with fab -R '<role to run command on, e.g c2_1>' runCommand:<command to run>
		or to run on a specific host: fab -H '10.0.2.194:2222' runCommand:'hostname'"""
	results = ''
	with fabi.hide('output', 'running', 'warnings', 'aborts'), fabi.settings(warn_only=True):
		results = fabi.run(command)
	print(results)

@fabi.parallel
def prunCommand(command):
	"""run with fab -R '<role to run command on, e.g c2_1>' runCommand:<command to run>
		or to run on a specific host: fab -H '10.0.2.194:2222' runCommand:'hostname'"""
	results = ''
	with fabi.hide('output', 'running', 'warnings', 'aborts'), fabi.settings(warn_only=True):
		results = fabi.run(command)
	print(results)


def put(src,dst):
	fabi.put(src, dst)

@fabi.parallel
def pput(src,dst):
	fabi.put(src, dst)

def LED():
	fabi.run('echo 1 >> /sys/class/leds/beaglebone\:green\:usr2/brightness')
	time.sleep(5)
	fabi.run('echo 0 >> /sys/class/leds/beaglebone\:green\:usr2/brightness')
