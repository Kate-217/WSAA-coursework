from github import Github
import config
import requests 

apikey = config.git_key
g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

#getting the clone URL
repo = g.get_repo("Kate-217/aprivateone")
print(repo.clone_url)

# getting the file url
file_info = repo.get_contents("test.txt")
url_file = file_info.download_url
print (url_file)

response = requests.get(url_file)
file_content = response.text
print(f"This is in the file: {file_content}")

new_content = file_content + " I have just added this line via VS Code \n"
print (new_content)

