
import sys

def hello_name():
    # Check if a name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <name>")
        return

    # Get the name from command line argument
    name = sys.argv[1]

    # Print the name to the console
    print("Hello,", name)


hello_name()
