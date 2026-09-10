import subprocess
import sys

if sys.argv[1] == "--commit":
    print("committing...")
    subprocess.Popen(["git", "commit", 
        "-am", "\"automated\""])