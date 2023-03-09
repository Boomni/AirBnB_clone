#!/usr/bin/env python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
