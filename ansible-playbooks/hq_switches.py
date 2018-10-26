#!/usr/bin/env python

import pexpect
import sys

from config import settings #needs config.py and values in sample settings.yaml

child = pexpect.spawn('ssh ' + settings["switch01"]["host"])
#child.logfile = sys.stdout
child.expect('User Name:')
child.sendline(settings["switch01"]["user"])
child.expect('Password:')
child.sendline(settings["switch01"]["password"])
child.expect('MLZ-SF300-48LP-1#')
child.sendline('terminal datadump')
child.expect('MLZ-SF300-48LP-1#')
child.sendline('sh run')
fout = file('aus-switch01.txt','w')
child.logfile = fout
child.expect('MLZ-SF300-48LP-1#')
print child.before
child.sendline('exit')

child = pexpect.spawn('ssh ' + settings["switch02"]["host"])
#child.logfile = sys.stdout #uncomment to see progress in stout
child.expect('User Name:')
child.sendline(settings["switch02"]["user"])
child.expect('Password:')
child.sendline(settings["switch02"]["password"])
child.expect('MLZ-SF300-48LP-2#')
child.sendline('terminal datadump')
child.expect('MLZ-SF300-48LP-2#')
child.sendline('sh run')
fout = file('aus-switch02.txt','w')
child.logfile = fout
child.expect('MLZ-SF300-48LP-2#')
print child.before
child.sendline('exit')

child = pexpect.spawn('ssh ' + settings["switch03"]["host"])
#child.logfile = sys.stdout
child.expect('User Name:')
child.sendline(settings["switch03"]["user"])
child.expect('Password:')
child.sendline(settings["switch03"]["password"])
child.expect('MLZ-SF300-48LP-3#')
child.sendline('terminal datadump')
child.expect('MLZ-SF300-48LP-3#')
child.sendline('sh run')
fout = file('aus-switch03.txt','w')
child.logfile = fout
child.expect('MLZ-SF300-48LP-3#')
print child.before
child.sendline('exit')
