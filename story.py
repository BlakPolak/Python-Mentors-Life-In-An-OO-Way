import random
import time
import os
from codecool_class import CodecoolClass


def main():
    os.system("clear")
    day_index = 0
    print("\033[1m"+"Uploading list of mentors..."+"\033[0m", "\nMentors are initialized!")
    print("\033[1m"+"\nUploading list of students..."+"\033[0m", "\nStudents are initialized!")
    time.sleep(2)
    codecool_krk = CodecoolClass.create_local_school()
    codecoolObject = CodecoolClass("Tennessee", 2048, codecool_krk[0], codecool_krk[1])
    print("\033[1m"+"\nCreating local school ..."+"\033[0m",
          "\nIn the near future not that far away...", codecoolObject.location, "in year", codecoolObject.year, ".")
    time.sleep(2)
    print("""
    In Tennessee a very rich man who wanted to be even richer created a technology park in which young talented adepts
    are invited to learn how to code. It's a place in which an experiment is happening. Once entering you are given a quest.
    You meet a group of uncertain about their humanity androids and you are asked to help to program them in such a way
    so that they felt more human - alike. The price is high - we need more programming teachers and there is less and less
    humans due to plague of laziness created, ironically by technology development ... Once a level of humanity is acquired
    the Mentor Android will be sent to new Codecool School to teach a class of extraordinary programmers.
    """)
    time.sleep(3)
    os.system('clear')
    print("\033[1m"+"Ordinary school day is full of events. We start by checking students energy level. "
          "Let's see who's been programming all night! "+"\033[0m", "\nChecking class energy level ...")
    time.sleep(2)
    codecoolObject.check_overall_energy()
    print("\033[1m"+"\nEnergy level drops dramatically down! We need someone who wakes us up immediately!"+"\033[0m")
    time.sleep(2)
    print("One of our mentor will be doing daily gymnastics with our class. Finding mentor... ")
    random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 3)]))
    time.sleep(2)
    random_mentor.do_gymnastics(codecoolObject.students)
    time.sleep(2)
    print("\033[1m"+"\nLet's code something! Searching for random student to do coding dojo ... "
                    "\nSomeone's gonna cry like a baby!"+"\033[0m")
    time.sleep(3)
    random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 3)]))
    student_for_dojo1 = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
    while True:
        student_for_dojo2 = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
        if student_for_dojo1 is not student_for_dojo2:
            random_mentor.do_coding_dojo(student_for_dojo1, student_for_dojo2)
            break
    time.sleep(3)
    codecoolObject.check_overall_energy()
    print("Coding dojos cost a lot of energy, but what the students wouldn't do to cheer their mentors up?!")
    os.system('clear')
    print("\033[1m"+"Meanwhile in the kitchen… "+"\033[0m")
    time.sleep(2)
    print("Time for small talk! Mentor drinking coffee with student. They both gets some points to energy level. "
          "Miracle at coffee machine!")
    random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 3)]))
    student_for_coffee = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
    random_mentor.drink_coffee_with_student(student_for_coffee)
    time.sleep(2)
    print("Lunch break is over, time to go back to learning! \nChecking overall energy level in class ...")
    codecoolObject.check_overall_energy()
    time.sleep(2)
    os.system('clear')
    print("\033[1m"+"Sometimes there is a need for tension breaker. Joke time!\nFunny as always!"+"\033[0m")
    random_mentor.say_joke(codecoolObject.students[random.randint(0, 5)])
    os.system("clear")
    print("\033[1m"+"\nBad energy level in the group! Looking for mentor with outstanding psychological qualities! "
          "\nFinding mentor... "+"\033[0m")
    time.sleep(3)
    random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
    time.sleep(1)
    random_mentor.give_motivational_speech(codecoolObject.students)
    os.system("clear")
    print("\033[1m"+"Mentors care about every student. If you have a problem - ask mentor. Day by day..."+"\033[0m")
    while not codecoolObject.is_any_mentor_became_human():
        day_index += 1
        print("\033[44mDay {}                                                           \033[0m".format(day_index))
        for mentor in codecoolObject.mentors:
            mentor_action = random.randint(0, 3)
            student = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
            if mentor_action == 0:
                while True:
                    student2 = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
                    if student is not student2:
                        mentor.do_coding_dojo(student, student2)
                        break
            elif mentor_action == 1:
                mentor.give_private_mentoring(student)
            elif mentor_action == 2:
                mentor.say_joke(student)
            else:
                mentor.drink_coffee_with_student(student)
        input("Enter to continue ...")
        os.system('clear')

if __name__ == "__main__":
    main()

