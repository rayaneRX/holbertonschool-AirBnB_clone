<p align=center>
<img src = "https://a0.muscache.com/airbnb/static/logos/belo-400x400.png" />
</p>


# <p align=center >`AirBnB clone - The console`</p>
## <p align=center> `Project's obejectives` </p>
Be able to explain:
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## <p align=center> `First step: Write a command interpreter to manage your AirBnB objects.` </p>
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## <p align=center> `What’s a command interpreter?` </p>
It’s exactly the same as the Shell, but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## <p align=center> `Resources` </p>
Read or watch:

- [cmd module](https://intranet.hbtn.io/rltoken/_mUwX-Mn69bDBP5iTQmCJA)
- [uuid module](https://intranet.hbtn.io/rltoken/4HNpF8nsTMociNaTgMYAeQ)
- [datetime](https://intranet.hbtn.io/rltoken/xnmMG0Qin2K9CxXdmQoZkA)
- [unittest module](https://intranet.hbtn.io/rltoken/MKNUT1FRSdUiGIpwMmrtgw)
- [args/kwargs](https://intranet.hbtn.io/rltoken/mY-8n8I-ohQIjkUOqcK6Rw)
- [Python test cheatsheet](https://intranet.hbtn.io/rltoken/9PsyQoeiVNhWGcj_1PkZJg)


## <p align=center> `Execution` </p>
The shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```bash
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

## <p align=center>`Tasks`</p>
### <p align=center>`0. README, AUTHORS`</p>
- Write a README.md:
  - description of the project
  - description of the command interpreter:
    - how to start it
    - how to use it
    - examples
- You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
- You should use branches and pull requests on GitHub - it will help you as team to organize your work
-------------------------------------------------------------------------------
### <p align=center>`1. Be pycodestyle compliant!`</p>
Write beautiful code that passes the pycodestyle checks.

-------------------------------------------------------------------------------
### <p align=center>`2. Unittests`</p>
All your files, classes, functions must be tested with unit tests

-------------------------------------------------------------------------------
### <p align=center>`3. BaseModel`</p>
Write a class BaseModel that defines all common attributes/methods for other classes:

- models/base_model.py
- Public instance attributes:
  - id: string - assign with an uuid when an instance is created:
    - you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
    - the goal is to have unique id for each BaseModel
  - created_at: datetime - assign with the current datetime when an instance is created
  - updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
- __str__: should print: [<class name>] (<self.id>) <self.__dict__>
- Public instance methods:
  - save(self): updates the public instance attribute updated_at with the current datetime
  - to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
    - by using self.__dict__, only instance attributes set will be returned
    - a key __class__ must be added to this dictionary with the class name of the object
    - created_at and updated_at must be converted to string object in ISO format:
      - format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
      - you can use isoformat() of datetime object
    - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
-------------------------------------------------------------------------------
### <p align=center>`4. Create BaseModel from dictionary`</p>
Update models/base_model.py:

- __init__(self, *args, **kwargs):
  - you will use *args, **kwargs arguments for the constructor of a BaseModel. (more information inside the AirBnB clone concept page)
  - *args won’t be used
  - if kwargs is not empty:
    - each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute. See the example output, below)
    - each value of this dictionary is the value of this attribute name
    - Warning: created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime
  - otherwise:
    - create id and created_at as you did previously (new instance)
-------------------------------------------------------------------------------
### <p align=center>`5. Store first object`</p>
Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:

- models/engine/file_storage.py
- Private class attributes:
  - __file_path: string - path to the JSON file (ex: file.json)
  - __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
- Public instance methods:
  - all(self): returns the dictionary __objects
  - new(self, obj): sets in __objects the obj with key <obj class name>.id
  - save(self): serializes __objects to the JSON file (path: __file_path)
  - reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Update models/__init__.py: to create a unique FileStorage instance for your application

- import file_storage.py
- create the variable storage, an instance of FileStorage
- call reload() method on this variable
Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage

- import the variable storage
- in the method save(self):
  - call save(self) method of storage
- __init__(self, *args, **kwargs):
  - if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
-------------------------------------------------------------------------------
### <p align=center>`6. Console 0.0.1`</p>
Write a program called console.py that contains the entry point of the command interpreter:

- You must use the module cmd
- Your class definition must be: class HBNBCommand(cmd.Cmd):
- Your command interpreter should implement:
  - quit and EOF to exit the program
  - help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
  - a custom prompt: (hbnb)
  - an empty line + ENTER shouldn’t execute anything
- Your code should not be executed when imported

You should end your file with:
```bash
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
