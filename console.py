#!/usr/bin/env python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


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
        """
        Creates a new instance of BaseModel, saves it to JSON file,
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

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Eg: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_instructions.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            obj_dict = storage.all()
            if obj_id in obj_dict:
                print(obj_dict[obj_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Eg: $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_instructions.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            obj_dict = storage.all()
            if obj_id in obj_dict:
                del obj_dict[obj_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based on or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        result = []
        obj_dict = storage.all()
        for key, value in obj_dict.items():
            if not arg:
                result.append(str(value))
            else:
                if value.__class__.__name__ == arg:
                    result.append(str(value))
        print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_instructions.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[0] + "." + args[1]
            obj_attribute_key = args[0] + "." + args[2]
            obj_attribute_value = args[3]
            not_accepted = ["id", "created_at", "updated_at"]
            obj_dict = storage.all()
            if obj_id not in obj_dict:
                print("** no instances found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif len(args) > 4:
                pass
            else:
                if args[2] in not_accepted:
                    pass
                else:
                    obj_dict[obj_id].__dict__[obj_attribute_key] = obj_attribute_value
                    obj_dict[obj_id].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
