#!/usr/bin/env python3
# Enter your code for "Steganography" here.

def tonum(byte):
	final = count = 0

	for bit in byte:
		final |= bit << count
		count += 0o10

	return final

img = open("ncss-modified.bmp", "rb")

# Move to header location detailing location of data
img.seek(0xA)
datap = tonum(img.read(4))

# Get image height and width
img.seek(0xE)
dib_tp = tonum(img.read(4))

height = 0
width = 0
bpp = 24

if dib_tp == 40:
	img.seek(0x12)
	width = tonum(img.read(4))

	img.seek(0x16)
	height = tonum(img.read(4))

	img.seek(0x1C)
	bpp = tonum(img.read(2))

elif dib_tp == 12:
	img.seek(0x12)
	width = tonum(img.read(2))

	img.seek(0x14)
	height = tonum(img.read(2))

	img.seek(0x18)
	bpp = tonum(img.read(2))

import math
rowsize = int(math.floor((bpp*width+31)/32)*4)
padding = int(rowsize - (bpp*width)/8)

# Go to data section
img.seek(datap)

rows = []
for row in zip(*[iter(img.read())]*rowsize):
	striprow = row
	for x in range(padding):
		striprow = striprow[:-1]
	for x in striprow:
		rows.append(x)

data = list(zip(*[iter(rows)]*8))

out = [""]
while out[-1] != "\x00":
	part = data.pop(0)
	# Get lowest significant bit for each 8-bit chunk
	bits = "".join([str(x & 0b1) for x in part][::-1])

	# Convert to chr
	out.append(chr(int(bits, 2)))

# Remove non-printable characters
out = [x for x in out if x != "\x00"]
print("".join(out))
