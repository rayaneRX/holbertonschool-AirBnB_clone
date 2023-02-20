#!/usr/bin/env python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """exit thr program"""
        return True

    def do_EOF(self, arg):
        """exit thr program with EOF """

    def do_help_quit(self, arg):
        """help to qiut """
        print("Quit command to exit the program")

    def do_help_EOF(self, arg):
        """help to EOF"""
        print("EFO command to exit the program")

    def emply_line(self, arg):
        """execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
