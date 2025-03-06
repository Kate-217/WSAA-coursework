from github import Github
import config 

apikey = config.git_key
g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

repo = g.get_repo("Kate-217/aprivateone")
print(repo.clone_url)
