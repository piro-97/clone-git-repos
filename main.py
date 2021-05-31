import os
import argparse
import re


def find_repo_name(url):
    """
        from url: 'https://github.com/<github_username>/<repo_name>'
        returns (<github_username>, <repo_name>)
    """
    names = url.split("/")  # github_username = names[3]; repo_name = names[4]
    
    if len(names) < 5:
        print("Invalid url supplied: ", url)
        return ("", "")

    return ( names[3], names[4] )


# parsing argv
description = 'Clone a list of git repositories; fill repos.txt with the urls of the repos you want to clone; note that you must be logged in in your github account via SSH'
parser = argparse.ArgumentParser(description=description)
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


# actual cloning
url_base = "git@github.com:"     # base url for git repos (SSH)
try:
    with open("repo_urls.txt", "r") as f:
        for line in f.readlines():
            name = find_repo_name(line)
            repo_url = url_base + name[0] + "/" + name[1] + ".git"
            os.system("git clone " + repo_url) # running git clone command

except FileNotFoundError:
    os.system("touch repo_urls.txt")    # creating empty repo_urls.txt
    print("repo_urls.txt is empty, please insert at least one repo url")
