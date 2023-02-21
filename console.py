#!/usr/bin/env python3
"""program called console.py that contains
the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """program called console.py that contains
    the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """exit thr program"""
        print("bay bay -From Rayane")
        return True

    def do_EOF(self, arg):
        """exit thr program with EOF """
        print()
        return True

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_help_quit(self, arg):
        """help to qiut """
        print("Quit command to exit the program")

    def do_help_EOF(self, arg):
        """help to EOF"""
        print("EOF command to exit the program")

    def do_help_create(self, arg):
        """help to create"""
        print("""'create' command creates an instant of BaseModel if you add
              class as argument after it""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
