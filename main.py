import os
import subprocess

# Clone the repository
repo_url = "https://github.com/carlospolop/hacktricks.git"
subprocess.run(["git", "clone", repo_url])

# Install Pandoc and LaTeX
subprocess.run(["sudo", "apt", "install", "-y", "pandoc"])
subprocess.run(["sudo", "apt", "install", "-y", "texlive", "texlive-xetex"])

# Convert the files to a single PDF
repo_folder = "hacktricks"
os.chdir(repo_folder)

find_files_command = "find . -name '*.md' | sort"
find_files = subprocess.Popen(find_files_command, stdout=subprocess.PIPE, shell=True)
files_to_convert = find_files.stdout.read().decode("utf-8").strip().split("\n")

pandoc_command = ["pandoc", "-s", "--pdf-engine=xelatex", "-o", "output.pdf"] + files_to_convert
subprocess.run(pandoc_command)

print("The output.pdf file has been generated in the hacktricks folder.")
