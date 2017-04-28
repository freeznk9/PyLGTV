#!/usr/bin/env python


import os.path
import string
import sys
import io
import time

sys.path += [os.path.dirname(__file__)]
import lgtv

"""
# examples
lgtv.Power('on')
time.sleep(5)
print lgtv.Power('status')
time.sleep(5)
lgtv.Power('off')
"""

if len(sys.argv) < 3 :
  print ("need args. ex : " + sys.argv[0] + " + power on/off/status, mute on/off/status, volume 0-25/status ")
  exit(1)

cmd1 = sys.argv[1]
cmd_data = sys.argv[2]

if(cmd1=="power") :
  if cmd_data=="on" :
    print lgtv.Power('on')
  elif cmd_data=="off" :
    print lgtv.Power('off')
  elif cmd_data=="status" :
    print lgtv.Power('status')
  else :
    print "wrong params."
    exit(1)
elif(cmd1=="volume") :
  if cmd_data=="status" :
    print lgtv.Volume('status')
  else :
    print lgtv.Volume(cmd_data)
elif(cmd1=="mute") :
  if cmd_data=="on" :
    print lgtv.Mute('on')
  elif cmd_data=="off" :
    print lgtv.Mute('off')
  elif cmd_data=="status" :
    print lgtv.Mute('status')
  else :
    print "wrong params."
    exit(1)
