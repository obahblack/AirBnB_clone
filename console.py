#!/usr/bin/python3
"""
Entry to command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Entry to command interpreter
    """
    prompt = "(hbnb)"
    classes = {"BaseModel", "State", "City", "Amenity",
               "Place", "Review", "User"}

    def do_EOF(self, line):
        """Exit on Ctrl-D"""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit"""
        return True

    def emptyline(self):
        """Overwrite defualt behavior to repeat last cmd"""
        pass

    def do_create(self, line):
        """Create instance specified by user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Print string representation: name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, line):
        """Destory instance specified by user; Save change to JSON file"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        args = line.split()
        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
            print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Update if given exact object, exact attriibute"""
        args = parse(line)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")

            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) \
                not in storage.all().keys():
            print("** not instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, line):
        """Display count of instances specified"""
        if line in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Accepts class name followed by argument"""
        # Split the line into 2 part: class_arg and command with arg(s)
        args = line.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(line))
            return
        # Extract the command and argment(s)
        try:
            args = args[1].split('(')
            command = args[0]
            if command = 'all':
                # Call do_all method with class_arg as argument
                HBNBCommand.do_count(self, class_arg)
            elif command == 'count':
                # Call do_count method with class_arg as argument
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                # Extract the id_arg from the command argument
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                # Concatenate class_arg and id_arg
                arg = class_arg + ' ' + id_arg
                # Call do_show method with arg as argument
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                # Extract the id_arg from the command argument
                args = args[1].split(')')
                id_args = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                # Concatenate class_arg and id_arg
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                # Extract the id_arg, name__arg, and val_arg
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = args.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg_strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                # Concatenate class_arg, id_arg, name_arg, and val_arg
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' \
                    + val_arg
                # Call do_update method with arg as argument
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


def parse(line):
    """Helper method to parse user typed input"""
    return tuple(line.split())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
