#!/usr/bin/env python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that inherits from cmd.Cmd class
    """
    prompt = "(hbnb) "
    class_instructions = {"BaseModel": BaseModel,
                          "User": User,
                          "State": State,
                          "City": City,
                          "Amenity": Amenity,
                          "Place": Place,
                          "Review": Review}

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
                not_accepted = ["id", "created_at", "updated_at"]
                obj_attr_value = args[3]
                obj_attr_key = args[0] + "." + args[2]
                if args[2] in not_accepted:
                    pass
                else:
                    obj_dict[obj_id].__dict__[obj_attr_key] = obj_attr_value
                    obj_dict[obj_id].save()

    def default(self, line):
        """
        Overriding the default method to handle <class_name>.command()
        """
        class_name, sep, command = line.partition('.')
        if sep == '.' and command == 'all()':
            self.do_all(class_name)
        elif sep == "." and command == "count()":
            self.do_count(class_name)
        elif sep == "." and command[:5] == "show(":
            extracted_id = command[6:-2]
            show_message = "{} {}".format(class_name, extracted_id)
            self.do_show(show_message)
        elif sep == "." and command[:8] == "destroy(":
            extracted_id = command[9:-2]
            destroy_message = "{} {}".format(class_name, extracted_id)
            self.do_destroy(destroy_message)
        elif sep == '.' and command[:7] == "update(":
            pattern = r'^(\w+)\.(\w+)\("(\w+)",\s*"(\w+)",\s*(\w+)\)$'
            s = line
            match = re.match(pattern, s)
            class_name = match.group(1)
            cmd = match.group(2)
            class_id = match.group(3)
            attr_key = match.group(4)
            attr_value = match.group(5)
            print(class_name, cmd, class_id, attr_key, attr_value)
        else:
            print('*** Unknown syntax:', line)

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            count = 0
            obj_dict = storage.all()
            for key, value in obj_dict.items():
                if not arg:
                    result.append(str(value))
                else:
                    if value.__class__.__name__ == args[0]:
                        count += 1
            print(count)
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
