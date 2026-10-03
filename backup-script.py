import subprocess
import sys

# cd ~/p/am-app
# python backup-script.py --commit
if sys.argv[1] == "--commit":
    print("committing...")
    subprocess.Popen(["git", "commit", 
        "-am", "automated11"])
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

# cd ~/p/am-app
# python backup-script.py --push-origin
if sys.argv[1] == "--push-origin":
    print("git push -u origin main")
    subprocess.Popen(["git", "push",
        "-u", "origin", "main"])

if sys.argv[1] == "--clone-bare-regular":
    print("cloning the bare repo into a regurlar repo")
    subprocess.Popen(["git", "clone",
        "/Users/seanusick/fd-git-backup/am-app.git",
        "am-app"])

# cd /Volumes/DISK_IMG/git-fd-backup/am-app
# python /Users/seanusick/p/am-app/backup-script.py --git-pull
if sys.argv[1] == "--git-pull":
    print("pull changes into flash drive")
    subprocess.Popen(["git", "pull"])

# cd /Volumes/DISK_IMG/git-fd-backup/
# python /Users/seanusick/p/am-app/backup-script.py --clone-bare


if sys.argv[1] == "--clone-bare2":
    print("Clone an existing repository into a bare repository2")
    subprocess.Popen(["git", "clone",
        "--bare", "/D/git-fd-backup/am-app",
        "/c/Users/seand/fd-git-backup/am-app.git"])

# cd ~/p
if sys.argv[1] == "--clone-bare-regular":
    print("cloning the bare repo into a regurlar repo")
    subprocess.Popen(["git", "clone",
        "/c/Users/seand/fd-git-backup/am-app.git",
        "am-app"])