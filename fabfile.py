import fabric.api as fabi
import fabric.operations as fop
from hosts import *
import time

#fabi.env.password="sd-writer"
#fabi.env.user="sd-writer"

#fabi.env.password="riaps"
#fabi.env.user="riaps"

fabi.env.key_filename = '~/.ssh/cluster_2018_9_10'
fabi.env.port = 222

fabi.env.skip_bad_hosts = True
fabi.env.warn_only = True
fabi.env.abort_on_prompts=True

def add_swapfile():

    # fop.sudo(cmd %"echo test > test.text")
    fop.run("tmux new -d -s swap")
    cmd = "tmux send -t swap '%s' ENTER"
    fop.run(cmd %"sudo fallocate -l 1G /swapfile")
    fop.run(cmd %"sudo dd if=/dev/zero of=/swapfile bs=1024 count=1048576")
    fop.run(cmd %"sudo chmod 600 /swapfile")
    fop.run(cmd %"sudo mkswap /swapfile")
    fop.run(cmd %"sudo swapon /swapfile")
    fop.run(cmd %'echo "/swapfile swap swap defaults 0 0" | sudo tee -a  /etc/fstab')

def update():
    fop.run("tmux new -d -s update")
    cmd = "tmux send -t update '%s' ENTER"
    fop.run(cmd %"sudo apt-get update")
    fop.run(cmd %"sudo apt-get install -y \"riaps-*\"")



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
        fabi.run('echo 1 | sudo tee -a /sys/class/leds/beaglebone\:green\:usr2/brightness')
        time.sleep(5)
        fabi.run('echo 0 | sudo tee -a /sys/class/leds/beaglebone\:green\:usr2/brightness')
