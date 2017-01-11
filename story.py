from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student


codecool_krk = CodecoolClass.create_local_school()
codecoolObject = CodecoolClass("Krakow", 2016, codecool_krk[0], codecool_krk[1])
codecoolObject.find_student_by_full_name("Marek Frankowicz")
codecoolObject.find_mentor_by_full_name("Przemek Ciacka")
codecoolObject.check_overall_energy()
codecoolObject.do_gymnastics(codecool_krk[1][0])
codecoolObject.give_motivational_speech(codecool_krk[1][0])
