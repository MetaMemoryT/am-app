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