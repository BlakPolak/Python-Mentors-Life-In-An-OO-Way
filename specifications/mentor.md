# Mentor

## Description
This class represents mentors.

## Parent class
Person

## Attributes

* ```nickname```
  * data type: string
  * description: stores the secret nickname of a mentor
* ```energy_level```
   * data type: integer
   * description: stores level of mentors energy.
* ```humanity_level```
  * data type: integer
  * description: stores  level of mentors humanity
  
## Class methods
### ```create_by_csv```
Creates a Mentor Object from csv file
#### Arguments
* csv file path

#### Return value

All the data needed to instantiate a mentor object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All data from Person and all of the arguments of the class itself.

#### Return value
None

### ```is_loving_gymnastic```
Check student mood for gymnastic (Good/Bad)
#### Arguments
* ```mood_for_gymnastic```
  * data_type: int
  * description: describes level of student mood for gymnastic.

#### Return value
Boolean

### ```is_paying_attention```
Checks student desire for getting new knowledge (Good/Bad)
#### Arguments
* ```knowledge_desire```
  * data_type: int
  * description: describes level of student knowledge desire.

#### Return value
Boolean

### ```do_gymnastic```
Mentor do gymnastic with student and that can increase or decrease students energy level and mentor humanity level.
#### Arguments
* ```students```
  * data_type: list of objects
  * description: describes students attributes

#### Return value
None

### ```give_motivational_speech```
Mentor give motivational speech for student and that can increase or decrease students energy level, students knowledge level and mentor humanity level.
#### Arguments
* ```students```
  * data_type: list of objects
  * description: describes students attributes

#### Return value
None

### ```give_private_mentoring```
Mentor give private mentoring for student and that can increase or decrease students energy level, students knowledge level and mentor humanity level.

#### Arguments
* ```student```
  * data_type: class instance object
  * description: describes student attributes

#### Return value
None

### ```drink_coffee_with_students```
Mentor drink coffee with student and that can increase or decrease students energy level, students knowledge level and mentor humanity level.

#### Arguments
* ```student```
  * data_type: class instance object
  * description: describes student attributes

#### Return value
None

### ```do_coding_dojo```
Mentor do coding dojo for two students and that can increase or decrease students energy level, students knowledge level and mentor humanity level.

#### Arguments
* ```student1```

  * data_type: class instance object
  * description: describes first student attributes
 
* ```student2```

  * data_type: class instance object
  * description: describes second student attributes

#### Return value
None

### ```say_joke```
Mentor say joke and that can increase or decrease students energy level, students knowledge level and mentor humanity level.

#### Arguments
* ```student```
  * data_type: class instance object
  * description: describes student attributes

#### Return value
None