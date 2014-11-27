#!/usr/bin/python

'''
Get deb depends recursive
'''


import sys
import commands

pkgs=[]

name=sys.argv[1]


def get_deps(name):
    status, output = commands.getstatusoutput("apt-cache depends %s | grep \"Depends:\" | awk \'{print $2}\'" % name)
    if output and status==0: 
        return status, output.split('\n')
    return status, []


def get_all_deps(name):
    global pkgs
    status, deps = get_deps(name)
    if deps and status==0:
        for n in deps:
            if n not in pkgs:
                pkgs.append(n)
                get_all_deps(n)
    return


get_all_deps(name)
print "\n".join(pkgs)
