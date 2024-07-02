#!/bin/bash
dir1="$1"
dir2="$2"
echo "Executing rsync delete"
rsync -av --delete "$dir1" "$dir2"
if [ $? -eq 0 ]; then
  echo "Complete!"
else
  echo "The command failed!"
fi
