#!/usr/bin/env python3

import pyperclip
import time
import sys

time.sleep(15)
if len(sys.argv) > 1:
  pyperclip.copy(sys.argv[1])
else:
  pyperclip.copy('')
exit()
