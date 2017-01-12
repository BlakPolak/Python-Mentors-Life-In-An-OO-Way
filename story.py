import random
import time
import os
#import csv
#import student
from codecool_class import CodecoolClass


def main():
    day_index = 0
    print("\033[1m"+"Uploading list of mentors..."+"\033[0m", "\nMentors are initialized!")
    print("\033[1m"+"\nUploading list of students..."+"\033[0m", "\nStudents are initialized!")
    time.sleep(2)
    codecool_krk = CodecoolClass.create_local_school()
    codecoolObject = CodecoolClass("Tennessee", 2048, codecool_krk[0], codecool_krk[1])
    print("\033[1m"+"Creating local school ..."+"\033[0m",
          "\nIn the near future not that far away: ", codecoolObject.location, "year:", codecoolObject.year)
    time.sleep(3)
    print("""
    In Tennessee a very rich man who wanted to be even richer created
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
    codecoolObject.check_overall_energy()
    print("\033[1m"+"\nEnergy level drops dramatically down! We need someone who wakes us up immediately!"+"\033[0m")
    time.sleep(1)
    print("One of our mentor doing daily gymnastics with our class. Finding mentor... ")
    randomMentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
    time.sleep(1)
    randomMentor.do_gymnastics(codecoolObject.students)
    time.sleep(1)
    print("Checking overall energy level in class ...")
    time.sleep(1)
    codecoolObject.check_overall_energy()
    time.sleep(1)
    print("\033[1m"+"\nSearching for random student to coding dojo ... \nSomeones gonna cry like a baby!"+"\033[0m")
    time.sleep(1)
    codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
    time.sleep(1)
    randomMentor.do_coding_dojo()
    os.system('clear')
    print("\033[1m"+"Meanwhile in the kitchen… "+"\033[0m")
    time.sleep(1)
    print("Time for small talk! Mentor drinking coffee with student.")
    time.sleep(1)
    print("Lunch break is over, time to go back to learning! \nChecking energy overall energy level in class ...")
    codecoolObject.check_overall_energy()
    time.sleep(1)
    codecoolObject.check_overall_energy()
    time.sleep(1)
    os.system('clear')
    print("\033[1m"+"Sometimes there is a need for tension breaker. Joke time!"+"\033[0m")
    randomMentor.say_joke()
    print("\033[1m"+"\nLooking for mentor with outstanding psychological qualities! Finding mentor... "+"\033[0m")
    time.sleep(1)
    randomMentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
    time.sleep(1)
    randomMentor.give_motivational_speech(codecoolObject.students)

    while not codecoolObject.mentor_became_human():
        day_index += 1
        print("\nDay {}".format(day_index))
        randomMentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
        mentor_action = random.randint(0, 3)
        student = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
        if mentor_action == 0:
            while True:
                student2 = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
                if student.last_name != student2.last_name:
                    randomMentor.do_coding_dojo(student, student2)
                    break
        elif mentor_action == 1:
            randomMentor.give_private_mentoring(student)
        elif mentor_action == 2:
            randomMentor.say_joke(student)
        else:
            student = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
            randomMentor.drink_coffee_with_student(student)
        time.sleep(2)

if __name__ == "__main__":
    main()

