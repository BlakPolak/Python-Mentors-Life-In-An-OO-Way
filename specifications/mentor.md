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