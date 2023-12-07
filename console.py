#!/usr/bin/python3
"""Command-line interface for Airbnb project"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Command interpreter for Airbnb project"""
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Display help messages"""
        cmd.Cmd.do_help(self, arg)

    def do_quit(self, arg):
        """Exit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF"""
        print()  # Print a newline for a clean exit
        return True
    
    def emptyline(self):
       """Do nothing on empty input line (overrides default behavior)"""
       pass
   
    def precmd(self, line):   
        """Handle non-interactive mode by reading commands from a file or pipeline"""
        if not sys.stdin.isatty():  # Check if input is not from a terminal (non-interactive mode)
            print(line)  # Print the command for better visibility
        return line

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Non-interactive mode
       with open(sys.argv[1], 'r') as file:
           HBNBCommand(stdin=file).cmdloop()
    else:  # Interactive mode
        HBNBCommand().cmdloop()
