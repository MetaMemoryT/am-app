import subprocess
import sys

if sys.argv[1] == "--commit":
    print("committing...")
    subprocess.Popen(["git", "commit", 
        "-am", "automated3"])
if sys.argv[1] == "--clone-bare":
    print("Clone an existing repository into a bare repository")
    subprocess.Popen(["git", "clone",
        "--bare", "/Users/seanusick/p/am-app",
        "/Users/seanusick/fd-git-backup/am-app.git"])
if sys.argv[1] == "--branch":
    print("git branch -M main")
    subprocess.Popen(["git", "branch",
        "-M", "main"])
if sys.argv[1] == "--remote-add":
    print("git remote add origin")
    subprocess.Popen(["git", "remote",
        "add", "origin",
        "/Users/seanusick/fd-git-backup/am-app.git"])
if sys.argv[1] == "--push-origin":
    print("git push -u origin main")
    subprocess.Popen(["git", "push",
        "-u", "origin", "main"])