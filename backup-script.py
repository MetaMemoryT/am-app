import subprocess
import sys
import os


#  The Golden Rule: Push to a Bare Repository or a Non-Checked-Out Branch
# this script could use bare repositories or a non-checked-out branch.
# I am sticking with bare repositories for now.

# TODO pathname compression
# DONE mac-to-fd remote-set-url

def commit():
    print("changing dir to ~/p/am-app...")
    os.chdir("/Users/seanusick/p/am-app")
    print("committing...")
    subprocess.run(["git", "commit", 
        "-am", "automated25"])

# python /Users/seanusick/p/am-app/backup-script.py --commit
if sys.argv[1] == "--commit":
    commit()

if sys.argv[1] == "--clone-bare":
    print("Clone an existing repository into a bare repository")
    subprocess.run(["git", "clone",
        "--bare", "/Users/seanusick/p/am-app",
        "/Users/seanusick/fd-git-backup/am-app.git"])
if sys.argv[1] == "--branch":
    print("git branch -M main")
    subprocess.run(["git", "branch",
        "-M", "main"])
if sys.argv[1] == "--remote-add":
    print("changing dir to ~/p/am-app...")
    os.chdir("/Users/seanusick/p/am-app")
    print("git remote add origin")
    subprocess.run(["git", "remote",
        "add", "origin",
        "/Users/seanusick/fd-git-backup/am-app.git"])

def push_origin():
    print("changing dir to ~/p/am-app...")
    os.chdir("/Users/seanusick/p/am-app")
    print("git push -u origin main")
    subprocess.run(["git", "push",
        "-u", "origin", "main"])

# cd ~/p
# python /Users/seanusick/p/am-app/backup-script.py --push-origin
if sys.argv[1] == "--push-origin":
    push_origin()

if sys.argv[1] == "--clone-bare-regular":
    print("cloning the bare repo into a regurlar repo")
    subprocess.run(["git", "clone",
        "/Users/seanusick/fd-git-backup/am-app.git",
        "am-app"])

def git_pull():
    print("changing dir to  /Volumes/DISK_IMG/git-fd-backup/am-app...")
    os.chdir("/Volumes/DISK_IMG/git-fd-backup/am-app")
    print("pull changes into flash drive...")
    subprocess.run(["git", "pull"])

# python /Users/seanusick/p/am-app/backup-script.py --git-pull
if sys.argv[1] == "--git-pull":
    git_pull()

# cd /Volumes/DISK_IMG/git-fd-backup/am-app
# python /Users/seanusick/p/am-app/backup-script.py --git-rebase
if sys.argv[1] == "--git-rebase":
    print("rebase changes into flash drive")
    subprocess.run(["git", "config", "pull.rebase", "false"])

# cd /Volumes/DISK_IMG/git-fd-backup/am-app
# python /Users/seanusick/p/am-app/backup-script.py --switch-main
if sys.argv[1] == "--switch-main":
    print("git branch -M main")
    print("switch to the main branch")
    subprocess.run(["git", "switch", "main"])

# cd /Volumes/DISK_IMG/git-fd-backup/
# python /Users/seanusick/p/am-app/backup-script.py --clone-bare

def set_url_mac():
    print("changing dir to /Volumes/DISK_IMG/git-fd-backup/am-app...")
    os.chdir("/Volumes/DISK_IMG/git-fd-backup/am-app")
    print("remote set-url on mac")
    subprocess.run(["git", "remote",
        "set-url", "origin",
        "/Users/seanusick/fd-git-backup/am-app.git"])

if sys.argv[1] == "--remote-set-url-mac":
    set_url_mac()

# python3 /Users/seanusick/p/am-app/backup-script.py --mac-to-fd
if sys.argv[1] == "--mac-to-fd":
    print("commiting...")
    commit()
    print("pushing origin...")
    push_origin()
    print("set-url")
    set_url_mac()
    print("pulling...")
    git_pull()

### On windows computer
# cd ~
# python /d/git-fd-backup/am-app/backup-script.py --clone-bare2
if sys.argv[1] == "--clone-bare2":
    print("Clone the existing repository on the flash drive into a bare repository2")
    subprocess.run(["git", "clone",
        "--bare", "D:\\git-fd-backup\\am-app",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git"])

# cd ~/p
# python /d/git-fd-backup/am-app/backup-script.py --clone-bare-regular
if sys.argv[1] == "--clone-bare-regular":
    print("cloning the bare repo into a regurlar repo")
    subprocess.run(["git", "clone",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git",
        "am-app"])

# python /d/git-fd-backup/am-app/backup-script.py --remote-set-url
if sys.argv[1] == "--remote-set-url":
    print("changing dir to D:\\git-fd-backup\\am-app...")
    os.chdir("D:\\git-fd-backup\\am-app")
    print("remote set-url on windows")
    subprocess.run(["git", "remote",
        "set-url", "origin",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git"])

# python /d/git-fd-backup/am-app/backup-script.py --push-origin
if sys.argv[1] == "--push-origin-windows":
    print("changing dir to D:\\git-fd-backup\\am-app...")
    os.chdir("D:\\git-fd-backup\\am-app")
    print("git push -u origin main")
    subprocess.run(["git", "push",
        "-u", "origin", "main"])

# python /d/git-fd-backup/am-app/backup-script.py --remate-add-windows-2
if sys.argv[1] == "--remote-add-windows-2":
    print("changing dir to C:\\Users\\seand\\p\\am-app...")
    os.chdir("C:\\Users\\seand\\p\\am-app...")
    print("git remote add origin")
    subprocess.run(["git", "remote",
        "add", "origin",
        "C:\\Users\\seand\\git-fd-backup\\am-app.git"])

# python /d/git-fd-backup/am-app/backup-script.py --git-pull-windows
if sys.argv[1] == "--git-pull-windows":
    print("changing dir to C:\\Users\\seand\\p\\am-app...")
    os.chdir("C:\\Users\\seand\\p\\am-app")
    print("pull changes into windows computer working repo...")
    subprocess.run(["git", "pull"])