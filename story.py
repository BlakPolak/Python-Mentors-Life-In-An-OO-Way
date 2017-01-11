from codecool_class import CodecoolClass
import random
import time
from mentor import Mentor
from student import Student


print("Uploading list of mentors („Mentors are initialized from CSV”)")
print("Uploading list of students („Students are initialized from CSV”)")
time.sleep(2)
codecoolObject = CodecoolClass("Krakow", 2016, codecool_krk[0], codecool_krk[1])
codecool_krk = CodecoolClass.create_local_school()
print(codecool_krk)
codecoolObject.find_student_by_full_name("Marek Frankowicz")
codecoolObject.find_mentor_by_full_name("Przemek Ciacka")
codecoolObject.check_overall_energy()
codecoolObject.do_gymnastics(codecool_krk[1][random.randint(0, 2)])
codecoolObject.give_motivational_speech(codecool_krk[1][random.randint(0, 2)])
