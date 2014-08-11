#!/usr/bin/env python3
# Enter your code for "Degree Distribution" here.

import csv

studentd = open("students.csv")
degreesd = open("degrees.csv")

students = []
courses = {}

class Student():
	def __init__(self, name, score, prefs):
		self.name = name
		self.score = float(score) # 30.0 is the minimum score

		# Prefs is a list of form ["course+bonus", "course+bonus"]
		self.prefs = []
		self.bonus = {}
		for item in prefs[:9]:
			new = item.split('+')

			# There is a bonus score for this course
			if len(new) == 2:
				self.bonus[new[0]] = float(new[1])

			# Add preference
			self.prefs += [new[0]]

		self.course = None

	def _get_bonus(self, course):
		# Get the bonus for a course
		newscore = self.score + self.bonus.get(course, 0)
		return min(newscore, 99.95) # 99.95 is the upper limit

	def get_best_pref(self):
		# Go though courses, in order of preference, and return first free course
		for crs in self.prefs:
			course = courses.get(crs)

			if not course:
				continue

			if course.is_ok(self):
				return crs

		# No courses left
		return None

	def auto_course(self):
		# Do the whole add course thing automagically

		new_pref = self.get_best_pref()

		# No remaining available courses
		if new_pref is None:
			self.course = None

		# Add student to course
		else:
			courses[new_pref].add_student(self)

class Course():
	def __init__(self, id, name, institution, places):
		self.id = id
		self.name = name
		self.institution = institution
		self.places = int(places)

		# Default students
		self.students = []
		self.cutoff = None

	def update_cutoff(self):
		# Sort by highest (bonus'd) score and then by alphabetical order
		self.students.sort(key=lambda S:(-S._get_bonus(self.id), S.name))

		# No students
		if not self.students:
			self.cutoff = None

		# Update cutoff to last student's bonus score
		else:
			self.cutoff = self.students[-1]._get_bonus(self.id)

	def is_ok(self, student):
		# Temporary student list, for checking ok-ness of student
		tmp_students = sorted(self.students + [student], key=lambda s:(-s._get_bonus(self.id), s.name))

		# Too many students?
		if len(tmp_students) > self.places:

			# Is the student still last?
			if student is tmp_students.pop():
				return False

		# Otherwise, student can join
		return True

	def add_student(self, student):
		# Student can't join, gtfo
		if not self.is_ok(student):
			return

		# Append student and sort them
		self.students += [student]
		self.students.sort(key=lambda s:(-s._get_bonus(self.id), s.name))

		# Update student's course id
		student.course = self.id

		# Too many students
		if len(self.students) > self.places:
			# Get last student
			update_student = self.students.pop()

			# Re-add student to their next preference
			new_pref = update_student.get_best_pref()
			if new_pref is None:
				update_student.course = None
			else:
				courses[new_pref].add_student(update_student)

for line in csv.DictReader(studentd):
	students += [Student(line["name"], line["score"], line["preferences"].split(";"))]

for line in csv.DictReader(degreesd):
	courses[line["code"]] = Course(line["code"], line["name"], line["institution"], line["places"])

students.sort(key=lambda S:(-S.score, S.name))
for student in students:
	student.auto_course()

for course in courses:
	courses[course].update_cutoff()

import sys

degrees = sorted(courses.values(), key=lambda C:C.id)
dwriter = csv.DictWriter(sys.stdout, fieldnames=["code", "name", "institution", "cutoff", "vacancies"])
print("code,name,institution,cutoff,vacancies")
for degree in degrees:
	dwriter.writerow({"code" : degree.id, "name" : degree.name, "institution" : degree.institution, "cutoff" : ("%.2f" % degree.cutoff) if degree.cutoff is not None else "-", "vacancies" : "YN"[degree.places == len(degree.students)]})

print("")

swriter = csv.DictWriter(sys.stdout, fieldnames=["name", "score", "offer"])
print("name,score,offer")
for student in students:
	swriter.writerow({"name" : "%s" % student.name, "score" : "%.2f" % student.score, "offer" : "%s" % (student.course or "-")})
