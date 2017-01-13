# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

## Class methods

### ```create_local_school```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```
#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object

### ```check_overall_energy```
Displays energy for all school members
#### Arguments
None

#### Return value
None

### ```is_any_mentor_became_human```
Checks if mentor became human being (when his humanity_level variable reaches 10). 
#### Arguments
None

#### Return value
* ```True or False```
  * data_type: Boolean
  * desciption: True if mentor reaches humanity_level :10, False if not