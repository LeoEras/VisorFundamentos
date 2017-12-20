import git
import os

base_path = os.path.dirname(os.path.realpath(__file__))
git_url = "http://200.10.150.91/est_espol/Fundamentos"
dir_path = base_path + "\\master"
branches = []

try:
    for b in git.Repo.clone_from(git_url, dir_path).remotes.origin.fetch():
        branches.append(b.name.split("/")[1])
except git.exc.GitCommandError:
    repo = git.Repo(dir_path)
    for b in repo.remotes.origin.fetch():
        branches.append(b.name.split("/")[1])
        
for item in branches:
    if "master" in item:
        continue
    else:
        try:
            dir_path = base_path + "\\" + item
            git.Repo.clone_from(git_url, dir_path, branch=item)
        except:
            dir_path = base_path + "\\" + item
            repo = git.Repo(dir_path)
            o = repo.remotes.origin
            o.pull()
