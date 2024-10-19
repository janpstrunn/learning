#!/bin/bash
# Script Sample to manage different commands
# After being thrown at the /usr/bin it's executable by commandline anywhere
case "$1" in
    "1")
        # Run an AppImage
        /path/to/your/appimage
        ;;
    "2")
        # Run an AppImage with optional arguments
        /path/to/your/appimage --option1 value1 --option2 value2
        ;;
    "3")
        # Run a compiled binary
        /path/to/your/binary
        ;;
    "4")
        # Run a compiled binary with optional arguments
        /path/to/your/binary --option1 value1 --option2 value2
        ;;
    "5")
        /path/to/script.sh
        # Run a custom script         
        ;;
    "6")
        # Run a custom script with optional arguments
        /path/to/your/script.sh "$2" "$3"
        ;;
    "7")
        # Run a full command with its arguments
        echo "Hello, world!"
        ;;
    "8")
        # Run a command using the provided variables
        echo "User input: $2"
        ;;
    "9")
        # Run an interactive command that requires user input
        read -p "Enter a value: " userInput
        echo "You entered: $userInput"
        ;;
    "10")
        # Run a command and redirect the output to a file
        ls -l > output.txt
        ;;
    "11")
        # Run a command and pipe its output to another command
        ls -l | grep "file"
        ;;
    "12")
        # Run a command conditionally based on success or failure of the previous command
        command1 && command2    # Run command2 only if command1 succeeds
        ;;
    *)
        echo -e "Reminder:\n 1 - AppImage\n 2 - Binary\n 3 - Script\n 4 - ..."
        exit 1
        ;;
esac
