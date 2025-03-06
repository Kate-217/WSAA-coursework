from github import Github
import config 

apikey = config.git_key
g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

#getting the clone URL
repo = g.get_repo("Kate-217/aprivateone")
print(repo.clone_url)

#file_info = repo.get_contents("WSAA-coursework/labs/test.txt")
#url_file = file_info.download_url
#print (url_file)