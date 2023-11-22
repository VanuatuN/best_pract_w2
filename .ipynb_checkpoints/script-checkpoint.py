# Stage 1: Handle Command Line

import sys

def parse_command_line():
    if len(sys.argv) != 2:
        print("Usage: python script.py <function_number>")
        sys.exit(1)
    
    try:
        function_number = int(sys.argv[1])
        return function_number
    except ValueError:
        print("Please provide a valid integer for function number.")
        sys.exit(1)

if __name__ == "__main__":
    function_number = parse_command_line()
    print(f"Selected function number: {function_number}")