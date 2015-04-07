# -*- encodig: utf-8 -*-i
#/bin/bash/python

import glob
import json
import random
from pprint import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Status:
	def __init__(self, a_new, a_review, a_completed):
		self.new = a_new
		self.review = a_review
		self.completed = a_completed
	def correct(self):
		self.new = self.new - 1
		self.review = self.review + 1
		if self.new == 0:
			self.completed = self.completed + 1
	def __str__(self):
		return "Stats:\n\nNew:%d\nReview:%d\nCompleted:%d\n" % (self.new, self. review, self.completed)

def wait():
	raw_input("Press [ENTER] to start:\n")

def learn(json_data):
	data_len = len(json_data["data"])
	status = Status( data_len, 0, 0)
	print(status)
	wait()
	array = range(0, data_len)
	print(array)
	while True:
		index = random.choice(array)
		item = json_data["data"][index]
		question = item["question"] + ": "
		answer = item["answer"]
		response = raw_input(question)
		if response == answer:
			print(bcolors.OKGREEN + "Correct answer!\n" + bcolors.ENDC)
			array = [x for x in array if x != index]
			status.correct()
		else:
			print(bcolors.FAIL + "Wrong answer!!!\nAnswer: %s" % answer + bcolors.ENDC)
		print(status)
		if len(array) == 0:
			break

def fight():
	pass

def test():
	pass

def choose():
	option = raw_input("Choose [1] Learn, [2] Fight, [3] Test or [4] Exit:")
	
	return option

option = choose()

while True:
	if option in ["1", "2", "3", "4"]:
		break
	else:
		option = choose()
	
sheets = glob.glob("*.json")

choose_sheet = "Please choose one bellow:\n"

for i, file in enumerate(sheets):
	choose_sheet = ""
	with open(file) as json_file:
		sheet_data = json.load(json_file)
		choose_sheet = choose_sheet + str(i) + ") " + sheet_data["title"] + "\n"

print(choose_sheet)
sheet_option = raw_input("Your choice:")


while True:
	if int(sheet_option) < len(sheets):
		break
	else:
		sheet_option = raw_input("Your choice:")

index = int(sheet_option)

with open(sheets[index]) as json_file:
	data = json.load(json_file)

if int(option) == 1:
	learn(data)
