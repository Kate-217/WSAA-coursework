from github import Github
import config1
import requests

apikey = config1.git_key
g = Github(apikey)

# Cheking out the repo
for repo in g.get_user().get_repos():
    print(repo.name)
    
file_path = "assignments/story.txt"    

#getting the clone URL
repo = g.get_repo("Kate-217/WSAA-coursework")
print(repo.clone_url) 


# getting the file url
file_info = repo.get_contents(file_path)
url_file = file_info.download_url
print (f'File URL: {url_file}')

response = requests.get(url_file)
content = response.text
print("Content of the file:", content)


new_content = content.replace("Andrew", "Kate")    

#updating file on githab
gitHubResponse=repo.update_file(
    file_path, # path 
    "updated by prog", # commit message
    new_content, # new content
    file_info.sha) 
print (gitHubResponse)

#repo.update_file(file_path, "Reverted to original version", content, file_info.sha)
