#!/usr/bin/env python3

### Modules ###

import os
import subprocess
import readline

###############

### Directories ###

pandora = "/run/media/janpstrunn/Pandora/"
obsidian = "Obsidian/"
forgejo = "Forgejo/"

####################

print("Available repos:\n")
subprocess.run(["lsd", pandora + forgejo], check=True)
subprocess.run(["lsd", pandora + obsidian], check=True)

p_j_output = subprocess.run(["ls", pandora + forgejo], text=True, check=True, capture_output=True).stdout.splitlines()
p_o_output = subprocess.run(["ls", pandora + obsidian], text=True, check=True, capture_output=True).stdout.splitlines()

directories = p_j_output + p_o_output

def completer(text, state):
    options = [d for d in directories if d.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

git_repo_dir = input("\nWhat git repo do you want to commit?\n")

obsidian_repos = {"YGGDRASIL", "LAPLACE", "OUROBOROS"}

if git_repo_dir in obsidian_repos:
    full_obsidian_path = os.path.join(pandora, obsidian, git_repo_dir + "/")

    commit_message = input("Enter your commit message:\n")

    try:
        subprocess.run(["git", "-C", full_obsidian_path, "add", "-A"], check=True)
        subprocess.run(["git", "-C", full_obsidian_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", full_obsidian_path, "push", "origin", "main"], check=True)
        print("Changes committed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

else:
    full_path = os.path.join(pandora, forgejo, git_repo_dir + "/")

    commit_message = "Auto Update"

    try:
        subprocess.run(["git", "-C", full_path, "add", "-A"], check=True)
        subprocess.run(["git", "-C", full_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", full_path, "push", "origin", "main"], check=True)
        print("Changes committed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
