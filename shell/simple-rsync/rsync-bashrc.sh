#!/bin/bash

# To use, add or source this script to .bashrc

alias delrsync="rsync -av --delete $1 $2"
alias updtrsync="rsync -av --update $1 $2"
