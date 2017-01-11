from codecool_class import CodecoolClass
import random
import time
import os
from mentor import Mentor
from student import Student


print("Uploading list of mentors („Mentors are initialized from CSV”)")
print("Uploading list of students („Students are initialized from CSV”)")
time.sleep(2)
codecool_krk = CodecoolClass.create_local_school()
codecoolObject = CodecoolClass("Krakow", 2016, codecool_krk[0], codecool_krk[1])
<<<<<<< HEAD
print(codecoolObject.location, codecoolObject.year, "Creating local school ...")
time.sleep(3)
print("""
        In the near future not that far away… In Tennessee a very rich man who wanted to be even richer created
        a technology park in which young talented adepts are invited to learn how to code. It's a place in which
        an experiment is happening. Once entering you are given a quest. You meet a group of uncertain about their
        humanity androids and you are asked to help to program them in such a way so that they felt more human - alike.
        The price is high - we need more programming teachers and there is less and less humans due to plague of
        laziness created ironically by technology development… Once a level of humanity is acquired the Mentor Android
        is will being sent to new Codecool School to teach new class of extraordinary programmers. In our school
        teaching 4 mentors and programming 6 students
""")
time.sleep(1)
os.system('clear')
print("Checking class energy level ...")
time.sleep(1)
print("Energy level status: . We need someone who wakes us up immidiatelly!")
time.sleep(1)
print("Finding mentor(One of our mentor doing daily gymnastics with our class)...")
codecoolObject.find_mentor_by_full_name(str(codecool_krk[1][random.randint(0, 2)]))
time.sleep(1)
codecoolObject.do_gymnastics(codecool_krk[1][random.randint(0, 2)])
time.sleep(1)
print("Checking energy overall energy level in class ...")
time.sleep(1)
codecoolObject.check_overall_energy()
os.system('clear')
print("Meanwhile in the kitchen… ")
time.sleep(1)
print("Drinking coffee and small talk ...")
time.sleep(1)
print("Checking energy overall energy level in class ...")
time.sleep(1)
codecoolObject.check_overall_energy()
time.sleep(1)
os.system('clear')
print("Finding mentor (Looking for mentor with outstanding psychological qualities...")
time.sleep(1)
codecoolObject.find_mentor_by_full_name(str(codecool_krk[1][random.randint(0, 2)]))
time.sleep(1)
codecoolObject.give_motivational_speech(codecool_krk[1][random.randint(0, 2)])
time.sleep(1)
codecoolObject.find_student_by_full_name(str(codecool_krk[0][random.randint(0, 6)]))


