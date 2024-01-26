#!/usr/bin/python3
"""Entry point to the application"""
import cmd
import importlib


class Ebookcmds(cmd.Cmd):
    """commands of the book will be 
    defined under this class"""
    prompt = "(eBook) "
    def do_quit(self, line):
        """Exit"""
        return True

    def help_quit(self):
        """shows info of quit command"""
        print("Command to exit the program")
        print("\n")

    def do_EOF(self, line):
        """Exit"""
        print()
        return True

    def help_EOF(self):
        """shows info about EOF command"""
        print("Command to exit the program\n", end=" ")
        print("\n")

    def emptyline(self):
        """When empty line is passed or  ENTER is pressed
        nothing should be  executed"""
        pass


if __name__ == '__main__':
    Ebookcmds().cmdloop()
