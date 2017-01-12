import random
import time
import os
from codecool_class import CodecoolClass


def main():
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
    humans due to plague of laziness created ironically by technology development… Once a level of humanity is acquired
    the Mentor Android is will being sent to new Codecool School to teach new class of extraordinary programmers.
    """)
    time.sleep(3)
    os.system('clear')
    print("\033[1m"+"Ordinary school day is full of events. We start by checking students energy level. "
          "Let's check who's programme all night! "+"\033[0m", "\nChecking class energy level ...")
    time.sleep(2)
    codecoolObject.check_overall_energy()
    print("\033[1m"+"\nEnergy level drops dramatically down! We need someone who wakes us up immediately!"+"\033[0m")
    time.sleep(2)
    print("One of our mentor doing daily gymnastics with our class. Finding mentor... ")
    random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
    time.sleep(2)
    random_mentor.do_gymnastics(codecoolObject.students)
    time.sleep(2)
    print("\033[1m"+"\nLet's code something! Searching for random student to coding dojo ... "
                    "\nSomeones gonna cry like a baby!"+"\033[0m")
    time.sleep(3)
    student_for_dojo = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
    time.sleep(3)
    random_mentor.do_coding_dojo(student_for_dojo, codecoolObject.students[random.randint(0, 5)])
    time.sleep(3)
    codecoolObject.check_overall_energy()
    print("Coding dojos cost a lot of energy, but what the students are not doing to cheer mentors!")
    os.system('clear')
    print("\033[1m"+"Meanwhile in the kitchen… "+"\033[0m")
    time.sleep(2)
    print("Time for small talk! Mentor drinking coffee with student. They both gets some points to energy level. "
          "Miracle at coffee machine!")
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
    print("\033[1m"+"Mentors care about each student. If you have a problem - ask mentor. Day by day..."+"\033[0m")
    while not codecoolObject.is_any_mentor_became_human():
        day_index += 1
        print("\nDay {}".format(day_index))
        random_mentor = codecoolObject.find_mentor_by_full_name(str(codecoolObject.mentors[random.randint(0, 2)]))
        mentor_action = random.randint(0, 3)
        student = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
        if mentor_action == 0:
            while True:
                student2 = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
                if student.last_name != student2.last_name:
                    random_mentor.do_coding_dojo(student, student2)
                    break
        elif mentor_action == 1:
            random_mentor.give_private_mentoring(student)
        elif mentor_action == 2:
            random_mentor.say_joke(student)
        else:
            student = codecoolObject.find_student_by_full_name(str(codecoolObject.students[random.randint(0, 5)]))
            random_mentor.drink_coffee_with_student(student)
        time.sleep(2)

if __name__ == "__main__":
    main()

