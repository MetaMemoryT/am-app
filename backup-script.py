import subprocess
import sys
import os


#  The Golden Rule: Push to a Bare Repository or a Non-Checked-Out Branch
# this script could use bare repositories or a non-checked-out branch.
# I am sticking with bare repositories for now.

# cd ~/p
# python /Users/seanusick/p/am-app/backup-script.py --commit
if sys.argv[1] == "--commit":
    print("changing dir to ~/p/am-app...")
    os.chdir("/Users/seanusick/p/am-app")
    print("committing...")
    subprocess.Popen(["git", "commit", 
        "-am", "automated19"])
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

# cd ~/p
# python /Users/seanusick/p/am-app/backup-script.py --push-origin
if sys.argv[1] == "--push-origin":
    print("changing dir to ~/p/am-app...")
    os.chdir("/Users/seanusick/p/am-app")
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

# cd /Volumes/DISK_IMG/git-fd-backup/am-app
# python /Users/seanusick/p/am-app/backup-script.py --git-rebase
if sys.argv[1] == "--git-rebase":
    print("rebase changes into flash drive")
    subprocess.Popen(["git", "config", "pull.rebase", "false"])

# cd /Volumes/DISK_IMG/git-fd-backup/am-app
# python /Users/seanusick/p/am-app/backup-script.py --switch-main
if sys.argv[1] == "--switch-main":
    print("git branch -M main")
    print("switch to the main branch")
    subprocess.Popen(["git", "switch", "main"])

# cd /Volumes/DISK_IMG/git-fd-backup/
# python /Users/seanusick/p/am-app/backup-script.py --clone-bare

### On windows computer
# cd ~
# python /d/git-fd-backup/am-app/backup-script.py --clone-bare2
if sys.argv[1] == "--clone-bare2":
    print("Clone the existing repository on the flash drive into a bare repository2")
    subprocess.Popen(["git", "clone",
        "--bare", "D:\\git-fd-backup\\am-app",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git"])

# cd ~/p
# python /d/git-fd-backup/am-app/backup-script.py --clone-bare-regular
if sys.argv[1] == "--clone-bare-regular":
    print("cloning the bare repo into a regurlar repo")
    subprocess.Popen(["git", "clone",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git",
        "am-app"])