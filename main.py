import os
import argparse

parser = argparse.ArgumentParser(description='Clone a list of git repositories; fill repos.txt with the names of the repos you want to clone')

parser.add_argument("github-username", help='username of your github account')
parser.add_argument("--output-dir", help='folder in which the repos will be cloned')

args = vars( parser.parse_args() )


try:
    out_dir = args["output-dir"]
except KeyError:
    out_dir = ""

# initialize output dir, creating it if it doesn't exist
out_path = os.getcwd() + "/" + out_dir
try:
    os.chdir(out_path)
except FileNotFoundError:
    os.mkdir(out_path)
    os.chdir(out_path)


url_base = "git@github.com:" + args["github-username"] +"/"     # base url for git repos (SSH)
try:
    with open("repos.txt", "r") as f:
        for repo_name in f.read().split():   # reading and splitting repo names
            repo_url = url_base + repo_name
            os.system("git clone " + repo_url + ".git") # running git clone command

except FileNotFoundError:
    os.system("touch repos.txt")    # creating empty repos.txt
    print("repos.txt is empty, please insert at least one repo name")