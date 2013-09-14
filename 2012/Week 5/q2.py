#!/usr/bin/env python2

def fix_yz(silly):
	silly = silly.replace("z","-abcd-")
	silly = silly.replace("y","z")
	silly = silly.replace("-abcd-","y")
	silly = silly.replace("Z","_abcd_")
	silly = silly.replace("Y","Z")
	silly = silly.replace("_abcd_","Y")
	return silly
