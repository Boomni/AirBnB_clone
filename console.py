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
        Usage: create <class name>
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
        Usage: show <class name> <class id>
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
        Usage: destroy <class_name> <class id>
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
        Usage: all <class_name> or all
            Eg: $ all BaseModel
                $ all
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
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Eg: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            $ update Place 1234-1234-1234 max_guest 34
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_instructions.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_id = args[1]
            obj_key = args[0] + "." + obj_id
            obj_dict = storage.all()
            if obj_key not in obj_dict:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = obj_dict[obj_key]
                if args[2][0] == '{' and args[-1][-1] == '}':
                    # dictionary representation
                    new_attrs = eval(" ".join(args[2:]))
                    if type(new_attrs) == dict:
                        for k, v in new_attrs.items():
                            if hasattr(obj, k):
                                v = type(getattr(obj, k))(v)
                                setattr(obj, k, v)
                        obj.save()
                    else:
                        print("** invalid format for dictionary representation **")
                else:
                    # attribute name and value
                    attr_name = args[2]
                    if hasattr(obj, attr_name):
                        attr_value = type(getattr(obj, attr_name))(args[3])
                        setattr(obj, attr_name, attr_value)
                        obj.save()
                    else:
                        print("'{}' object has no attribute '{}'".format(args[0], attr_name))

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
            if command[-2] == "}" and "{" in command:
                obj_id, sep, attr_dict = command.strip().partition(",")
                id_val = obj_id[8:-1]
                attr_dict = eval(attr_dict[:-1].lstrip())
                if attr_dict == -1:
                    print("** invalid format for dictionary representation **")
                    return
                for key, value in attr_dict.items():
                    update_message = "{} {} {} {}".format(class_name,
                                                          id_val,
                                                          str(key),
                                                          value)
                    print(update_message)
                    self.do_update(update_message)
            elif "{" not in command:
                arguments = command[7:-1].strip().split(",")
                id_val = arguments[0][1:-1]
                obj_attr_key = arguments[1]
                obj_attr_value = arguments[2]
                update_message = "{} {} {} {}".format(class_name,
                                                      id_val,
                                                      obj_attr_key,
                                                      obj_attr_value)
                self.do_update(update_message)
            else:
                print('*** Unknown syntax:', line)
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
