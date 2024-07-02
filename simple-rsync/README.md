# Simple rsync script

Don't expect it to be something else, but simple.

## simple-rsync-script.sh

Is a really simple shell script which allows you to run the following commands by opt: 

``rsync -av --delete "$dir1" "$dir2"`` or ``rsync -av --update "$dir1" "$dir2"``

*dir1 is the source directory and dir2 is the directory to receive changes.

After the command successful, you are presented with another option to run: ``diff -R "$dir1" "$dir2"``, which shows you, recursively, the differences in both directories.

## rsync-delete.sh

Is the script containing only the ``rsync -av --delete "$dir1" "$dir2"`` command.

Allows you to create a identical replica of the directory source, deleting everything in a folder that isn't in the source and updating all the older files

## rsync-update.sh

Is the script containing only the ``rsync -av --update "$dir1" "$dir2"`` command.

Allows you to only update all the files, adding the ones that are missing and updating the ones that are old.

## Required dependencies:
- rsync

## Usage:
Run the script, and give the directories path. The script must be executable.

Examples:

``./simple-rsync-script.sh path/to/directory path/to/directory``

``./simple-rsync-script.sh /$HOME/Downloads/ /$HOME/Documents/``

## Official rsync github: https://github.com/WayneD/rsync
