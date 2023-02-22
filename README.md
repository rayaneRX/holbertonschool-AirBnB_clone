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
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
    - This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel
-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
### <p align=center>``</p>

-------------------------------------------------------------------------------
