#!/usr/bin/python3

import fabric.api as fabi
import paramiko
import socket
from collections import OrderedDict

fabi.env.key_filename = '~/.ssh/cluster_2018_9_10'

fabi.env.skip_bad_hosts = True
fabi.env.warn_only=True
fabi.env.abort_on_prompts=True

fabi.env.port=222

def runCommand(command):
    """run with fab -R '<role to run command on, e.g c2_1>' runCommand:<command to run>
    or to run on a specific host: fab -H '10.0.2.194:2222' runCommand:'hostname'"""
    results = ''
    with fabi.hide('output', 'running', 'warnings', 'aborts'), fabi.settings(warn_only=True):
        results = fabi.run(command)
    return(results)

@fabi.task
def discoverHosts ():
    out = fabi.local("sudo arp-scan -I enp0s8 --localnet", capture=True).rsplit("\n")
    print("out")
    print(out)
    devices = out[2:-3]
    IPs = []
    ip2host ={}
    host2ip = {}
    for device in devices:
        ip = device.split("\t")[0]
        #out = fabi.execute(runCommand, 'hostname', hosts=ip+":2222")
        try:
            out = fabi.execute(runCommand, 'hostname', hosts=ip)
            # out = fabi.execute(runCommand, 'hostname', hosts=ip+":2222")
            key = list(out)[0]
            value = out[key]
            if 'bbb' in str(value):
                ip2host[key] = value
                host2ip[value] = key
                IPs.append(ip)
        except SystemExit as e :
            print("not mine")
            print(e)
        except paramiko.SSHException as e:
            print("Wrong ssh key")
            print(e)

    sortedHosts =  OrderedDict(sorted(host2ip.items(), key=lambda item: socket.inet_aton(item[1])))
    return sortedHosts

@fabi.task
def printHosts(hosts):
    for ix, host in enumerate(hosts):
        end = " " if (ix % 2==0) else "\n"
        print('"%s": "%s",' %(host, hosts[host]), end=end)

sortedHosts = discoverHosts()
printHosts(sortedHosts)
