from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student


codecool_krk = CodecoolClass.create_local_school()
codecoolObject = CodecoolClass("Krakow", 2016, codecool_krk)
codecoolObject.find_student_by_full_name("Marek Frankowicz")