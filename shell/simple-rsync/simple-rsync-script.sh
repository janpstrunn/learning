#!/bin/bash
dir1="$1"
dir2="$2"
read -p "Do you want to update the content or delete the data that isn't present in the source? (updt/del): " choice
if [ "$choice" = "updt" ]; then
    echo "Running rsync -av --update"
    rsync -av --update "$dir1" "$dir2"
    if [ $? -eq 0 ]; then
        echo "Complete!"
        read -p "Do you want to extra run a diff command to show directories differences? (y/n): " choice
        if [ "$choice" = "y" ]; then
            echo "Running diff"
            diff -r "$dir1" "$dir2"
            if [ $? -eq 0 ]; then
                echo "Complete!"
            fi
        else
            echo "Skipped"
        fi
    else
        echo "The command 'rsync' failed!"
    fi
elif [ "$choice" = "del" ]; then
    echo "Running rsync -av --delete"
    rsync -av --delete "$dir1" "$dir2"
    if [ $? -eq 0 ]; then
        echo "Complete!"
    else
        echo "The command 'rsync' failed!"
    fi
else
    echo "Invalid choice. Please choose 'updt' or 'del'."
fi
