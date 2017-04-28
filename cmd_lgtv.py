#!/usr/bin/env python


import os.path
import string
import sys
import io
import time

sys.path += [os.path.dirname(__file__)]
import lgtv

lgtv.Power('on')
time.sleep(5)
print lgtv.Power('status')
time.sleep(5)
lgtv.Power('off')

