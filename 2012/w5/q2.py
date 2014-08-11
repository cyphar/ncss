#!/usr/bin/env python2

import string
def fix_yz(silly):
	return silly.translate(string.maketrans("YyZz","ZzYy"))
