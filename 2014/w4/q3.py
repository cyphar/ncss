#!/usr/bin/env python3
# Enter your code for "Need to Go!" here.

import csv
import math

RADIUS = 6371000

class Position(object):
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def distance(self, other):
		phi1 = math.radians(self.latitude)
		lambda1 = math.radians(self.longitude)

		phi2 = math.radians(other.latitude)
		lambda2 = math.radians(other.longitude)

		sines = math.sin(phi1) * math.sin(phi2)
		coses = math.cos(phi1) * math.cos(phi2) * math.cos(abs(lambda1 - lambda2))

		sigma = math.acos(sines + coses)
		return RADIUS * sigma


def geo_degrees(geoloc):
	fields = geoloc.split()

	# Check field number.
	if len(fields) != 4:
		raise Exception("Invalid field number in geolocation.")

	# Get fields.
	deg, mini, sec = map(float, fields[:3])
	quad = fields[3]

	# Convert decimals.
	decimal = deg + (mini/60) + (sec/3600)

	# Deal with quadrants.
	if quad in ["S", "W"]:
		decimal = -decimal

	return decimal

def load_toilets(path):
	with open(path) as csvfile:
		for row in csv.DictReader(csvfile):
			yield row

def main():
	def toilet2position(toilet):
		latitude = float(toilet["Latitude"])
		longitude = float(toilet["Longitude"])

		return Position(latitude, longitude)

	latitude = geo_degrees(input())
	longitude = geo_degrees(input())
	time = int(input())

	userpos = Position(latitude, longitude)
	toilets = load_toilets("public-toilets.csv")

	opens = []
	for toilet in toilets:
		if toilet["IsOpen"] == "AllHours":
			opens.append(toilet)
			continue

		if toilet["IsOpen"] == "DaylightHours" and 6 <= time <= 20:
			opens.append(toilet)

	closest = min(opens, key=lambda t: userpos.distance(toilet2position(t)))
	distance = userpos.distance(toilet2position(closest))

	print("Closest toilet: %s, %s, %s" % (closest["Name"], closest["Town"], closest["State"]))
	print("Distance: %dkm" % (round(distance/1000)))

if __name__ == "__main__":
	main()
