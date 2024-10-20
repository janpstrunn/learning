#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog
import os
import subprocess

# Directories

pandora = "/run/media/janpstrunn/Pandora/"
obsidian = "Obsidian/"
forgejo = "Forgejo/"
p_j = os.path.join(pandora, forgejo)

print("Available repos:\n")
subprocess.run(["lsd", p_j], text=True, check=True)

git_repo_dir = input("\nWhat git repo do you want to commit?\n")

obsidian_repos = {"YGGDRASIL", "LAPLACE", "OUROBOROS"}

if git_repo_dir.lower() in obsidian_repos:
    full_obsidian_path = os.path.join(pandora, obsidian, git_repo_dir + "/")

    root = tk.Tk()
    root.withdraw()

    commit_message = simpledialog.askstring("Git Commit", "Enter your commit message:")

    try:
        subprocess.run(["git", "-C", full_obsidian_path, "add", "-A"], check=True)
        subprocess.run(["git", "-C", full_obsidian_path, "commit", "-m", commit_message], check=True)
        print("Changes committed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

else:
    full_path = os.path.join(p_j, git_repo_dir + "/")

    root = tk.Tk()
    root.withdraw()

    commit_message = simpledialog.askstring("Git Commit", "Enter your commit message:")

    try:
        subprocess.run(["git", "-C", full_path, "add", "-A"], check=True)
        subprocess.run(["git", "-C", full_path, "commit", "-m", commit_message], check=True)
        print("Changes committed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
