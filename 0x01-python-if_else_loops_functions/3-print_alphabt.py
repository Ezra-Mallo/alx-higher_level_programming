#!/usr/bin/python3
import sys
for xter in  range(97, 122):
    if xter != 101 and xter != 113:
        sys.stderr.write(chr(xter))
