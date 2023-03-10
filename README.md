# AirBnB Clone ― The console
---
## Project Description

>> The Console project is an assignment given as part of the Alx Africa Software Engineering course. 

>> It involves building a console application that mimics the functionality of the popular online accommodation booking platform, [Airbnb Website](https://www.airbnb.com/).

**The project requires an understanding of programming concepts and skills, such as:**
- data structures
- file input/output
- object-oriented programming, among others. 

>> The goal of the project is to create a working prototype of the application that allows users to create, view, and book accommodation listings. 

**The final version of this project will have:**
- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.
---
### Files and Directories
- ```models``` directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- ```tests``` directory will contain all unit tests.
- ```console.py``` file is the entry point of our command interpreter.
- ```models/base_model.py``` file is the base class of all our models. It contains common elements:
    - attributes: ```id```, ```created_at``` and ```updated_at```
    - methods: ```save()``` and ```to_json()```
- ```models/engine``` directory will contain all storage classes (using the same prototype). For the moment I will have only one: ```file_storage.py```.

**In summary, the steps in performing the AirBnB clone project are:**

- Creating a parent class called "BaseModel" that handles the initialization, serialization, and deserialization of future instances.
- Implementing the classes for the various AirBnB objects, inheriting from the BaseModel class.
- Creating a simple flow of serialization/deserialization involving an instance, dictionary, JSON string, and file.
- Creating an abstracted storage engine for file storage.
- Writing unit tests to validate all classes and storage engines.
- Creating a command interpreter in Python using the cmd module.
---
## Description of the command interpreter
### General Use

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. 

There are a variety of commands available within the console program.

| Commands  | Description |
| ------------- | ------------- |
| ```quit```  | Quits the console  |
| ```Ctrl+D```  | Quits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of type , saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an objects
| ```all or all <class>```  | Prints all string representations of all objects or Prints all string representations of all objects of a specific class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object with a certain attribute (new or existing)
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary representation of attribute names and values

## Examples

Shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
---
## Authors

- IZIREN ABIOLA JOSEPH <jospaco2001@yahoo.com>
- Jonthan Boomni <rejoiceoye1@gmail.com>
---
