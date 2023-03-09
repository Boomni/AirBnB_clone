#!/usr/bin/env python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd class
    """
    prompt = "(hbnb) "
    class_instructions = {"BaseModel": BaseModel}

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
    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file,
        and prints the id
        Eg: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_instructions.keys():
            print("** class doesn't exist **")
        else:
            the_class = eval(arg)()
            the_class.save()
            print(the_class.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
